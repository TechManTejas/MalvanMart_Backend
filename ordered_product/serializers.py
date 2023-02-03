from rest_framework import serializers
from .models import OrderedProduct


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = [
            "id",
            "name",
            "quantity"
        ]
