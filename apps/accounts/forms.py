from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from apps.accounts.models import CustomAccount
from apps.utils.custom_validators import (contains_lowercase,
                                          contains_special_symbols,
                                          contains_uppercase,
                                          contains_digits)


class AccountRegistrationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required
    fields, plus a repeated password. """

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               validators=[contains_uppercase,
                                           contains_digits,
                                           contains_lowercase,
                                           contains_special_symbols])
    password_confirm = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomAccount
        fields = ('email', 'username')

    def clean(self):
        # Check that the two password entries match
        if self.is_valid():
            password = self.cleaned_data["password"]
            password_confirm = self.cleaned_data["password_confirm"]
            if not password == password_confirm:
                raise ValidationError("Passwords don't match")

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
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
