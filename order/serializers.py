from rest_framework import serializers
from ordered_product.models import OrderedProduct
from ordered_product.serializers import OrderedProductSerializer
from product.models import Product
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
        amount = validated_data.pop('amount')
        items = []

        for item_data in items_data:
            product_data = item_data.pop('product')
            product = Product.objects.get(sku=product_data['sku'])
            item_data['product'] = product
            amount += item_data['quantity'] * product.discounted_price
            items.append(OrderedProduct.objects.create(**item_data))

        validated_data['amount'] = amount
        order = Order.objects.create(**validated_data)
        for item in items:
            order.items.add(item)

        return order
