from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
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
