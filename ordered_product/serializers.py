from rest_framework import serializers
from product.models import Product
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

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.get(sku=product_data['sku'])
        validated_data['product'] = product
        return OrderedProduct.objects.model(**validated_data)
