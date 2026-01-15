from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category


# function based view
def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "myapp/product_list.html", {"products": products})
