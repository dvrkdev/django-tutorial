from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Account created successfully!", extra_tags="success"
            )
            return redirect("home")
        else:
            messages.error(
                request, "An error occurred during registration.", extra_tags="danger"
            )
    else:
        form = UserCreationForm()
    return render(request, "registration/register_user.html", {"form": form})
