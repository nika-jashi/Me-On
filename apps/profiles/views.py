from django.shortcuts import render, redirect
from django.views import View

from apps.accounts.models import CustomAccount
from apps.profiles.forms import ProfileCustomisationForm, LinkCustomisationForm
from apps.profiles.models import Profile, SocialLink


class AccountProfileView(View):
    """ A view for a profile of a current account. """

    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        accounts_profile_name = CustomAccount.objects.filter(username=accounts_page_name).exists()
        accounts_profile = Profile.objects.filter(account__username=accounts_page_name).first()
        accounts_links = SocialLink.objects.filter(link_owner__username=accounts_page_name).values_list()
        context = {'accounts_profile': accounts_profile,
                   'accounts_links': accounts_links
                   }
        # Check If Username Exists In Database (If Exists Profile Should Be Automatically Generated)
        if not accounts_profile_name:
            return redirect('home')
        else:
            return render(request, 'profile/profile_of_account.html', context)


class Home(View):
    """ A view for a home page. """

    def get(self, request, *args, **kwargs):
        return render(request, 'home/home.html')


class ProfileCustomisationView(View):
    """ A view for a profile customisation of a current account. """

    template_name = 'profile/profile_customisation.html'

    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        current_account = request.user.username
        data_of_account = Profile.objects.get(account__username=current_account)
        form = ProfileCustomisationForm(instance=data_of_account)
        # Check If Current Account Is Really The Owner Of a Profile
        if not accounts_page_name == current_account:
            return redirect(f'/{request.user.username}/')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        account_profile = Profile.objects.get(account=request.user)
        form = ProfileCustomisationForm(request.POST, request.FILES, instance=account_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account = request.user
            profile.save()
            return redirect(f'/{request.user.username}/')
        else:
            return render(request, self.template_name, {"form": form})


class SocialLinkCustomisationView(View):
    template_name = 'profile/profile_link_add.html'

    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        current_account = request.user.username
        form = LinkCustomisationForm()
        if not accounts_page_name == current_account:
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LinkCustomisationForm(request.POST)
        link_owner_account = CustomAccount.objects.filter(email=request.user).first()
        if form.is_valid():
            social_link_form = form.save(commit=False)
            social_link_form.link_owner = link_owner_account
            social_link_form.save()

            return redirect(f'/{request.user.username}/')
        else:
            return render(request, self.template_name, {'form': form})


class SocialLinkUpdateView(View):
    template_name = 'profile/profile_link_edit.html'

    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        current_link_pk = self.kwargs['pk']
        current_account = request.user.username
        existing_pk = SocialLink.objects.filter(pk=current_link_pk).exists()
        link_pk = SocialLink.objects.get(pk=current_link_pk)
        form = LinkCustomisationForm(instance=link_pk)
        if accounts_page_name != current_account:
            return redirect(f'/{request.user.username}/')
        elif not existing_pk:
            return redirect(f'/{request.user.username}/')
        else:
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        current_link_pk = self.kwargs['pk']
        accounts_page_name = self.kwargs['username']
        existing_pk = SocialLink.objects.filter(pk=current_link_pk).first()
        form = LinkCustomisationForm(request.POST, instance=existing_pk)
        if form.is_valid():
            social_link_form = form.save(commit=False)
            social_link_form.save()

            return redirect(f'/{accounts_page_name}/')
        else:
            return render(request, self.template_name, {'form': form})


class SocialLinkDeleteView(View):
    template_name = 'profile/profile_link_delete.html'

    def get(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        current_link_pk = self.kwargs['pk']
        current_account = request.user.username
        existing_pk = SocialLink.objects.filter(pk=current_link_pk).exists()
        if accounts_page_name != current_account:
            return redirect(f'/{request.user.username}/')
        elif not existing_pk:
            return redirect(f'/{request.user.username}/')
        else:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        accounts_page_name = self.kwargs['username']
        if accounts_page_name == request.user.username:
            if request.POST.get('delete') == "delete":
                SocialLink.objects.filter(pk=self.kwargs['pk']).delete()
                return redirect(f'/{request.user.username}/')
            elif request.POST.get('no') == 'no':
                return redirect(f'/{request.user.username}/')
        return render(request, self.template_name)
