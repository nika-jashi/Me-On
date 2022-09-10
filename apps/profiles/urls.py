from django.contrib.auth.decorators import login_required as l
from django.urls import path
from apps.profiles.views import (AccountProfileView,
                                 Home,
                                 ProfileCustomisationView,
                                 SocialLinkCustomisationView,
                                 SocialLinkUpdateView,
                                 SocialLinkDeleteView)

urlpatterns = [
    path("<str:username>/", AccountProfileView.as_view(), name="account_profile"),
    path("<str:username>/edit-profile/", l(ProfileCustomisationView.as_view()), name="profile_customisation"),
    path("<str:username>/add-link/", l(SocialLinkCustomisationView.as_view()), name="link_creation"),
    path("<str:username>/edit-link/<int:pk>", l(SocialLinkUpdateView.as_view()), name="link_customisation"),
    path("<str:username>/delete-link/<int:pk>", l(SocialLinkDeleteView.as_view()), name="link_deletion"),
    path('', Home.as_view(), name='home'),

]
