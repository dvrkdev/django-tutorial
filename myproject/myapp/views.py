from django.views.generic import DetailView, ListView

from .models import Product


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
