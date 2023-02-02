from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer


class CategoryModelViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
