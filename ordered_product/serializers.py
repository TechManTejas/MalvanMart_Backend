from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import OrderedProduct


class OrderedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderedProduct
        fields = [
            "id",
            "product",
            "quantity"
        ]
