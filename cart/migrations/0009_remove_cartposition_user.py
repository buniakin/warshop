# Generated by Django 4.1.3 on 2022-11-29 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cartposition_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartposition',
            name='user',
        ),
    ]
