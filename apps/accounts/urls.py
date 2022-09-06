from django.urls import path
from apps.accounts.views import AccountRegistrationView, AccountAuthenticationView, AccountLogoutView

urlpatterns = [
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountAuthenticationView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    ]
