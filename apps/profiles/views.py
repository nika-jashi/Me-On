from django.shortcuts import render, redirect
from django.views import View

from apps.accounts.models import CustomAccount
from apps.profiles.forms import ProfileCustomisationForm, LinkCustomisationForm
from apps.profiles.models import Profile, SocialLink


class AccountProfileView(View):
    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        accounts_profile_name = CustomAccount.objects.filter(username=accounts_page_name).exists()
        accounts_profile = Profile.objects.filter(account__username=accounts_page_name).first()
        accounts_links = SocialLink.objects.filter(link_owner__username=accounts_page_name).values_list()
        context = {'accounts_profile': accounts_profile,
                   'accounts_links': accounts_links
                   }
        if not accounts_profile_name:
            return redirect('home')
        else:
            return render(request, 'profile/profile_of_account.html', context)


class Home(View):
    def get(self, request, *args, **kwargs):
        link_username = request.user.username
        if request.user.is_authenticated:
            return redirect(f'profile/{link_username}')
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


class SocialLinkCustomisationView(View):
    template_name = 'profile/profile_link_add.html'
    context_object = {"form": LinkCustomisationForm()}

    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        current_account = request.user.username
        if not accounts_page_name == current_account:
            return redirect('home')
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):
        form = LinkCustomisationForm(request.POST)
        link_owner_account = CustomAccount.objects.filter(email=request.user).first()
        if form.is_valid():
            social_link_form = form.save(commit=False)
            social_link_form.link_owner = link_owner_account
            social_link_form.save()

            return redirect('/')
        else:
            return render(request, self.template_name, self.context_object)
