from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from apps.accounts.forms import AccountRegistrationForm, AccountAuthenticationForm


class AccountRegistrationView(View):
    """ A view for creating new users. with proper form and redirection """
    template_name = 'account/account_registration.html'

    def get(self, request):
        form = AccountRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = AccountRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            return render(request, self.template_name, {'form': form})


class AccountAuthenticationView(View):
    """ A view for authenticating existing users. with proper form and redirection """
    template_name = 'account/account_login.html'

    def get(self, request, *args, **kwargs):
        form = AccountAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = AccountAuthenticationForm(data=request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')

        else:
            return render(request, self.template_name, {'form': form})


class AccountLogoutView(View):
    """ A view for authenticated users to log out """
    template_name = 'account/account_logout.html'

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return render(request, self.template_name)
