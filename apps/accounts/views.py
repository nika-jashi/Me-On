from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from apps.accounts.forms import AccountRegistrationForm, AccountAuthenticationForm


class AccountRegistrationView(View):
    template_name = 'account/account_registration.html'
    context_object = {"form": AccountRegistrationForm()}

    def get(self, request):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        form = AccountRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            return render(request, self.template_name, self.context_object)


class AccountAuthenticationView(View):
    template_name = 'account/account_login.html'
    context_object = {"form": AccountAuthenticationForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

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
            return render(request, self.template_name, self.context_object)


class AccountLogoutView(View):
    template_name = 'account/account_logout.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name)
