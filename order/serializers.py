from rest_framework import serializers
from ordered_product.serializers import OrderedProductSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    items = OrderedProductSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            "id",
            "items",
            "first_name",
            "last_name",
            "email",
            "phone",
            "street_address",
            "city",
            "country",
            "postal",
            "payment"
        ]
