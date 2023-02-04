from rest_framework import serializers
from ordered_product.models import OrderedProduct
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
            "payment",
            "amount"
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderedProduct.objects.create(order=order, **item_data)
        return order
