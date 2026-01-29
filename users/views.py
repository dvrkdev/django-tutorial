from django.contrib import messages
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
            messages.success(request, f"Account created for {username}!")
            return redirect("blog:home")
        else:
            messages.error(
                request, "Something went wrong. Please try again!", extra_tags="danger"
            )
    else:
        form = UserRegisterForm()
    return render(request, "users/register_user.html", {"form": form})
