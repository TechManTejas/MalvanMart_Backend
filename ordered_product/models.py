from django.db import models
from product.models import Product


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
