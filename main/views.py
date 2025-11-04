from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm


def function_view(request):
    return HttpResponse("This is a function view.")


class ClassView(View):
    def get(self, request):
        return HttpResponse("This is a class view.")


def index(request):
    form = ReservationForm()

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success!")

    return render(request, "index.html", {"form": form})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class HomeView(View):
    def get(self, request):
        return HttpResponse("Home")
