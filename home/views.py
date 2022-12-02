import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

import orders.views
from cart.models import CartPosition
from home.models import Person
from warshop.settings import CART_SESSION_KEY


def index(request):
    response = render(request, 'home/index.html', {
        'page_title': 'Main'
    })

    return response


def about(request):
    return render(request, 'home/about.html', {
        'page_title': 'About'
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'page_title': 'Contacts'
    })