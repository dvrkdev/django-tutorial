from django.urls import path
from . import views

urlpatterns = [
    path("function", views.function_view, name="function"),
    path("class", views.ClassView.as_view(), name="class"),
    path("", views.index, name="index"),
]
