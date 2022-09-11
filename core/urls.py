from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('real/admin/', admin.site.urls),

    path('accounts/', include('apps.accounts.urls')),
    path('', include('apps.profiles.urls')),
]
