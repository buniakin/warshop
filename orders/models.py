from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def ValidatePrice(value):
    if(value >= 0):
        return value
    else:
        raise ValidationError("This field must be positive")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, validators=[ValidatePrice])
    status = models.CharField(max_length=50)
