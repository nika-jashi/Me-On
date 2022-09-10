from django.db import models
from django.urls import reverse

from apps.accounts.models import CustomAccount


class SocialLink(models.Model):
    name = models.CharField(max_length=54)
    link = models.URLField(max_length=1000)
    link_owner = models.ForeignKey(to=CustomAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    account = models.OneToOneField(to=CustomAccount, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=54, blank=True)
    small_bio = models.TextField(max_length=140, blank=True)
    profile_picture = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.account.username
