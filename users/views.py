from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from users.forms import UserRegisterForm


# Create your views here.
def register_user(request) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created. You are now able to log in."
            )
            return redirect("users:login")
        else:
            messages.error(
                request, "Something went wrong. Please try again!", extra_tags="danger"
            )
    else:
        form = UserRegisterForm()
    return render(request, "users/register_user.html", {"form": form})


@login_required
def logout_view(request) -> HttpResponseRedirect:
    logout(request)
    return redirect("login")


@login_required
def profile_view(request) -> HttpResponse:
    return render(request, "users/profile.html")
