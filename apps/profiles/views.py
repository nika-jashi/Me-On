from django.shortcuts import render
from django.views import View

from apps.accounts.models import CustomAccount


class AccountProfileView(View):
    def get(self, request, username, *args, **kwargs):
        accounts_profile = CustomAccount.objects.filter(username=username).first()
        if not accounts_profile:
            return render(request, 'home/home.html')
        else:
            return render(request, 'profile/profile_of_account.html', {'accounts_profile': accounts_profile})


class Home(View):
    def get(self, request, *args, **kwargs):
        link_username = request.user.username
        return render(request, 'home/home.html', {'link_username': link_username})
