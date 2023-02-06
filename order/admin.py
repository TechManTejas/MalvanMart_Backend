from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "timestamp",
        "first_name",
        "last_name",
        "email",
        "phone",
        "street_address",
        "city",
        "country",
        "postal",
        "payment",
        "amount"
    ]
    readonly_fields = [
        "amount"
    ]