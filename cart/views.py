import json
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import *
from catalog.models import Product
from warshop.settings import CART_SESSION_KEY
from .cartCookie import CartCookie
from .models import *


def index(request):
    sessionKey = request.COOKIES.get("sessionForCarts")
    usersCartPositions = CartPosition.objects.filter(session=sessionKey).filter(status="cart")
    return render(request, 'cart/index.html', {
        'page_title': 'Cart', 'positions': usersCartPositions
    })


def remove(request, id):
    cartPosition = CartPosition.objects.get(id=id)
    if cartPosition:
        cartPosition.delete()
        return redirect(index)


def addToCart(request):
    if request.method == "GET":
        productId = int(request.GET["productID"])
        product = Product.objects.get(id=productId)
        cartKey = request.COOKIES.get(CART_SESSION_KEY)
        if (cartKey is None):
            key = request.session.session_key
            if (key is None):
                request.session.create()
                key = request.session.session_key
            cartKey = key
        if(CartPosition.objects.filter(session=cartKey, product_id=productId, status="cart")):
            return JsonResponse({'message': "Цей товар вже є в кошику!", "added": False})
        else:
            newCartPosition = CartPosition()
            newCartPosition.product = product
            newCartPosition.count = 1
            newCartPosition.totalPrice = product.price
            newCartPosition.session = cartKey
            newCartPosition.save()

            count = CartPosition.objects.filter(session=cartKey, status="cart").count()

            response = JsonResponse({'message': "Товар успішно додано!", 'count': count, 'added': True})

            response.cookies[CART_SESSION_KEY] = cartKey

            return response


def save(request):
    if request.method == "POST":

        positions = json.loads(request.POST["positions"])

        for position in positions:
            cartPosition = CartPosition.objects.get(id=position['id'])
            cartPosition.count = position['count']
            cartPosition.totalPrice = position['totalPrice']
            cartPosition.save()

        return HttpResponse(json.dumps({"message" : "Збереження пройшло успішно"}), content_type="application/json")


def getCount(request):
    if request.method == "GET":
        print("ok")
        sessionKey = request.COOKIES.get("sessionForCarts")
        if (sessionKey):
            count = CartPosition.objects.filter(session=sessionKey, status="cart").count()
            print(count)
            return HttpResponse(json.dumps({"status": True, "count": count}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": False, "count": None}), content_type="application/json")
    else:
        print("bad")
        return HttpResponse("BadRequest")
