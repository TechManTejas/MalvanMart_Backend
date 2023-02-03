from django.db import models
from product.models import Product

class Order(models.Model):
    items = models.ManyToManyField(Product)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)
