from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.urls import resolve

from apps.accounts.models import CustomAccount
from apps.profiles.forms import ProfileCustomisationForm
from apps.profiles.models import Profile, SocialLink


class AccountProfileView(View):
    def get(self, request, username, *args, **kwargs):
        accounts_profile_name = CustomAccount.objects.filter(username=username).first()
        accounts_page_name = self.kwargs['username']
        accounts_profile = Profile.objects.filter(account__username=accounts_page_name).first()
        context = {'accounts_profile': accounts_profile}
        if not accounts_profile_name:
            return render(request, 'home/home.html')
        else:
            return render(request, 'profile/profile_of_account.html', context)


class Home(View):
    def get(self, request, *args, **kwargs):
        link_username = request.user.username
        authenticated_account = request.user
        if authenticated_account:
            return redirect(f'account/{link_username}')
        else:
            return render(request, 'home/home.html')


class ProfileCustomisationView(View):
    template_name = 'profile/profile_customisation.html'
    context_object = {"form": ProfileCustomisationForm()}

    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        current_account = request.user.username
        if not accounts_page_name == current_account:
            return redirect('home')
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(account=request.user)
        form = ProfileCustomisationForm(request.POST, instance=profile)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('/')
        else:
            return render(request, self.template_name, self.context_object)
