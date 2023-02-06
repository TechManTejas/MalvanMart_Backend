from rest_framework import serializers
from category.models import Category

from category.serializers import CategorySerializer
from .models import  Product


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
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

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(**category_data)
        validated_data['category'] = category
        return Product.objects.create(**validated_data)

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "sku"
        ]
