from rest_framework import viewsets
from .models import OrderedProduct
from .serializers import OrderedProductSerializer


class OrderedProductModelViewset(viewsets.ModelViewSet):
    queryset = OrderedProduct.objects.all()
    serializer_class = OrderedProductSerializer
