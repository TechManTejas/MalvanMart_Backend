from django.db import models
from product.models import Product

class Order(models.Model):
    items = models.ManyToManyField(Product)

    def __str__(self):
        return self.items
