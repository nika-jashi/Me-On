from django.db import models
from apps.accounts.models import CustomAccount


class SocialLink(models.Model):
    name = models.CharField(max_length=54)
    link = models.URLField(max_length=1000)

    def __str__(self):
        return self.name


class Profile(models.Model):
    social_media_link = models.ForeignKey(to=SocialLink, on_delete=models.CASCADE, blank=True, null=True)
    account = models.OneToOneField(to=CustomAccount, on_delete=models.CASCADE)
    head_name = models.CharField(max_length=54)
    profile_picture = models.ImageField(upload_to='media/profile_images', blank=True, null=True)

    def __str__(self):
        return self.account.username
