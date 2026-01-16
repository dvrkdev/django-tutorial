from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
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


# user registration
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Registration successful. Welcome!", extra_tags="success"
            )
            return redirect("product_list")
        else:
            messages.error(
                request, "Please correct the errors below.", extra_tags="danger"
            )
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
