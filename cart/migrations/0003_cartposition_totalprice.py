# Generated by Django 4.1.3 on 2022-11-24 20:38

import cart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartposition_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartposition',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[cart.models.ValidatePrice]),
        ),
    ]
