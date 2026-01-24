# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from accounts.models import CustomUser


class HomeView(ListView):
    model = CustomUser
    template_name = "main/home.html"
    context_object_name = 'users'
    paginate_by = 10
