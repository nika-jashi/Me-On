import re

from django import forms
from django.contrib.auth import authenticate

from apps.accounts.models import CustomAccount
from apps.utils.custom_validators import (contains_lowercase,
                                          contains_uppercase,
                                          contains_digits, )


class AccountRegistrationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required
    fields, plus a repeated password. """

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               validators=[contains_uppercase,
                                           contains_digits,
                                           contains_lowercase],
                               required=True)
    password_confirm = forms.CharField(label='Password confirmation',
                                       widget=forms.PasswordInput,
                                       required=True)
    username = forms.CharField()

    class Meta:
        model = CustomAccount
        fields = ('email', 'username')

    def clean(self):
        taken_username = CustomAccount.objects.filter(username=self.cleaned_data['username']).exists()
        taken_email = CustomAccount.objects.filter(email=self.cleaned_data['email']).exists()
        # Check that the two password entries match
        if self.is_valid():
            password = self.cleaned_data["password"]
            password_confirm = self.cleaned_data["password_confirm"]
            username = self.cleaned_data['username']
            if password != password_confirm:
                self.add_error('password', "Passwords don't match")
            # Check That Username Exists Or Not
            if taken_username:
                self.add_error('username', 'This Username Is Already Taken')
            # Check That Email Exists Or Not
            if taken_email:
                self.add_error('email', 'This Email Is Already Taken')
            # Check that Username has valid characters
            if re.search(r"\W", username):
                self.add_error('username',
                               "This field must not contain at least one special character like: ! @ # $ % ^ & * _ + =")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomAccount
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            taken_email = CustomAccount.objects.filter(email=self.cleaned_data['email']).exists()
            if not taken_email:
                if not authenticate(email=email):
                    raise forms.ValidationError("Please Provide Valid Email")
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("password is incorrect")
