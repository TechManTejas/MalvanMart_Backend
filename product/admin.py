from django.contrib import admin
from .models import Product


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id", 
        "sku", 
        "name",
        "picture",
        "description",
        "in_stock",
        "price",
        "discounted_price",
        "category"
    ]
