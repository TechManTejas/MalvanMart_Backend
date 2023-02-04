from rest_framework import serializers
from product.serializers import CartProductSerializer
from .models import OrderedProduct


class OrderedProductSerializer(serializers.ModelSerializer):
    product = CartProductSerializer()
    class Meta:
        model = OrderedProduct
        fields = [
            "id",
            "product",
            "quantity"
        ]
