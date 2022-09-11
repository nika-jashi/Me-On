import re

from django import forms

from apps.profiles.models import Profile, SocialLink


class ProfileCustomisationForm(forms.ModelForm):
    small_bio = forms.CharField(max_length=140, help_text="Piece Of Information About You", widget=forms.Textarea,
                                required=False)
    full_name = forms.CharField(max_length=54, help_text="Put Your Real Name If You Want", required=False)
    profile_picture = forms.ImageField(help_text="upload Your Profile Photo", required=False)

    class Meta:
        model = Profile
        fields = ('full_name', 'small_bio', 'profile_picture')


class LinkCustomisationForm(forms.ModelForm):
    name = forms.CharField(max_length=54, help_text="Input Name Of The Site Or Indicator For URL")
    link = forms.URLField(max_length=100, help_text="Input URL Here")

    class Meta:
        model = SocialLink
        fields = ('name', 'link')

    def clean(self):
        name = self.cleaned_data['name']
        if not re.search(r'([\w !#%()-=&~])', name):
            raise forms.ValidationError('Please Provide Valid Name (Description)')
