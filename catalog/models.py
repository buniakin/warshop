from django.core.exceptions import ValidationError
from django.db import models


def ValidatePrice(value):
    if(value >= 0):
        return value
    else:
        raise ValidationError("This field must be positive")


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[ValidatePrice])
    image = models.ImageField(null=True,blank=True, upload_to="product_images/")

