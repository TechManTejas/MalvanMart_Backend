from django.db import models
from ordered_product.models import OrderedProduct


class Order(models.Model):
    PAYMENT_CHOICES = (
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Online', 'Online'),
    )

    items = models.ManyToManyField(OrderedProduct)
    first_name = models.CharField(default='', max_length=255)
    last_name = models.CharField(default='', max_length=255)
    email = models.EmailField(default='', max_length=255)
    phone = models.BigIntegerField(default=0)
    street_address = models.CharField(default='', max_length=255)
    city = models.CharField(default='', max_length=255)
    country = models.CharField(default='', max_length=255)
    postal = models.CharField(default='', max_length=255)
    payment = models.CharField(default='',choices=PAYMENT_CHOICES, max_length=255)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)
