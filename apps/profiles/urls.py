from django.contrib.auth.decorators import login_required as l
from django.urls import path
from apps.profiles.views import AccountProfileView, Home, ProfileCustomisationView, SocialLinkCustomisationView

urlpatterns = [
    path("profile/<str:username>/", AccountProfileView.as_view(), name="account_profile"),
    path("profile/<str:username>/edit/", l(ProfileCustomisationView.as_view()), name="profile_customisation"),
    path("profile/<str:username>/add-link/", l(SocialLinkCustomisationView.as_view()), name="link_customisation"),
    path('', Home.as_view(), name='home'),

]
