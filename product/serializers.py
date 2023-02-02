from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
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
