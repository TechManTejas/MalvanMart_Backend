from django.db import models
from category.models import Category
from tag.models import Tag


class Product(models.Model):
    sku = models.CharField(default='', max_length=255)
    name = models.CharField(default='', max_length=255)
    # picture = models.ImageField(upload_to="product/images")
    description = models.CharField(default='', max_length=255)
    in_stock = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.sku
