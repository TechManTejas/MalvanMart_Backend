from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductModelViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get')