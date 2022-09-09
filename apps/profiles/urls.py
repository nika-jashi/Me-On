from django.contrib.auth.decorators import login_required as l
from django.urls import path
from apps.profiles.views import AccountProfileView, Home, ProfileCustomisationView

urlpatterns = [
    path("account/<str:username>/", AccountProfileView.as_view(), name="account_profile"),
    path("account/<str:username>/edit/", l(ProfileCustomisationView.as_view()), name="profile_customisation"),
    path('', Home.as_view(), name='home'),

]
