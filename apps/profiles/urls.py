from django.urls import path, re_path
from apps.profiles.views import AccountProfileView, Home

urlpatterns = [
    path("account/<str:username>/", AccountProfileView.as_view(), name="account_profile"),
    path('', Home.as_view(), name='home'),

]
