from django.urls import path
from . import views

urlpatterns = [
    path("function/", views.function_view, name="function"),
    path("class/", views.ClassView.as_view(), name="class"),
    path("", views.index, name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("home/", views.HomeView.as_view(), name="home"),
    path('todo/list/', views.TodoListView.as_view(), name='todo-list'),
    path('todo/create/', views.TodoFormView.as_view(), name='todo-create-form'),
]
