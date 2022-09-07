from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Profile
from apps.accounts.models import CustomAccount


@receiver(post_save, sender=CustomAccount)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(account=instance)


@receiver(post_save, sender=CustomAccount)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
