from django import forms
from apps.profiles.models import Profile


class ProfileCustomisationForm(forms.ModelForm):
    social_media_link = forms.CharField(max_length=1000, required=False)

    class Meta:
        model = Profile
        fields = ('head_name', 'profile_picture')
