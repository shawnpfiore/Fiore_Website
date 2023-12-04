from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fiore_website.apps.public.urls')),
    path('accounts/', include('fiore_website.apps.accounts.urls')),
    path("contact/", include("fiore_website.apps.contact.urls")),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
