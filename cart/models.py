import json

from django.core.exceptions import ValidationError
from django.db import models

from django.contrib.auth.models import User
from catalog.models import Product
from orders.models import Order


def ValidatePrice(value):
    if(value >= 0):
        return value
    else:
        raise ValidationError("This field must be positive")


# Create your models here.
class CartPosition(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    orders = models.ManyToManyField(Order)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=10, validators=[ValidatePrice], default=0.00)
    status = models.CharField(max_length=50, default="cart")
    session = models.CharField(max_length=50, default="")

    def toJSON(self):
        return "{product_id:" + str(self.product.id) + ", count:" + str(self.count) + "}"
