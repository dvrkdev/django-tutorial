from django.contrib import admin

from .models import Category, Product

admin.site.site_header = "My Shop"
admin.site.index_title = "Dashboard"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "is_active"]
    list_filter = ["category", "is_active"]
    search_fields = ["name", "description"]
    list_editable = ["price", "is_active"]
