# from django.contrib.auth import views as auth_views
from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_user, name="register"),
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
]
