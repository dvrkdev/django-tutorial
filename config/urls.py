from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def home(request):
    return HttpResponse("home")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", home, name="home"),
]
