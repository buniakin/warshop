# Generated by Django 4.1.3 on 2022-11-25 08:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[orders.models.ValidatePrice])),
                ('status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]