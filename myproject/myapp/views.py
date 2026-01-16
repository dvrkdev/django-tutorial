from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


# # function based view
# def product_list(request):
#     products = Product.objects.filter(is_active=True)
#     return render(request, "myapp/product_list.html", {"products": products})


class ProductListView(ListView):
    model = Product
    template_name = "myapp/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = "myapp/product_detail.html"
    context_object_name = "product"
