from requests import Response
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer


class OrderModelViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ('post')
