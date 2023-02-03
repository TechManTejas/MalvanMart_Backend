from django.contrib import admin
from .models import OrderedProduct


@admin.register(OrderedProduct)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "quantity"
    ]
