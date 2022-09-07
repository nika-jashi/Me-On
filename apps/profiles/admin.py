from django.contrib import admin
from apps.profiles.models import Profile, SocialLink

admin.site.register(Profile)
admin.site.register(SocialLink)
