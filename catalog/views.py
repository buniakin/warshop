from django.shortcuts import render
from django.contrib import auth
from cart.models import CartPosition
from .models import *


def index(request):
    products = Product.objects.all()

    return render(request, 'catalog/index.html', {
        'page_title': 'Shopping', 'products': products
    })
