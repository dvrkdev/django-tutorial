from django import forms
from .models import Reservation, CustomUser, Todo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = [
            "username",
            "email",
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = [
            "username",
        ]


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]
