from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.register_user, name="register_user"),
]
