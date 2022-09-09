from django import forms
from apps.profiles.models import Profile, SocialLink


class ProfileCustomisationForm(forms.ModelForm):
    small_bio = forms.CharField(max_length=140, help_text="Piece Of Information About You", required=False)
    full_name = forms.CharField(max_length=54, help_text="Put Your Real Name If You Want", required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('small_bio', 'profile_picture', 'full_name')


class LinkCustomisationForm(forms.ModelForm):
    name = forms.CharField(max_length=54, help_text="name of the site", required=True)
    link = forms.URLField(max_length=100, help_text="Input URL Here", required=True)

    class Meta:
        model = SocialLink
        fields = ('name', 'link')
