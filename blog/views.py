# from django.shortcuts import render
from django.http import HttpResponse

# home view
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

# about view
def about(request):
    return HttpResponse('<h1>Blog About</h1>')
