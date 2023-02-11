from django.contrib import admin
from apps.accounts.models import CustomAccount

""" Registers model for admin in his/her panel. """
admin.site.register(CustomAccount)
