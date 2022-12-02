import decimal
import smtplib
from email.mime.text import MIMEText
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import orders
from cart.models import CartPosition
from orders.models import Order
from warshop.settings import MAIL_LOGIN, MAII_KEY


def sendmail(to, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(MAIL_LOGIN, MAII_KEY)
        msg = MIMEText(message)
        msg['Subject'] = "Order"
        server.sendmail(MAIL_LOGIN, to, msg.as_string())
    except Exception as _ex:
        print("Error of sending mail")


@login_required
def index(request):
    orders = Order.objects.filter(user_id=request.user.id)
    return render(request, 'orders/index.html', {
        'page_title': 'orders',
        'orders': orders
    })


@login_required
def order(request, id):
    order = Order.objects.get(id=id)
    positions = order.cartposition_set.all()
    return render(request, 'orders/order.html', {
        'page_title': 'order',
        'order': order,
        'cartPositions': positions
    })


@login_required
def check(request, id):
    order = Order.objects.get(id=id)
    positions = order.cartposition_set.all()
    return render(request, 'orders/check.html', {
        'page_title': 'orders',
        'order': order,
        'cartPositions': positions
    })


@login_required
def confirm(request):
    if request.method == "POST":
        order = Order.objects.get(id=request.POST["id"])
        positionsText = ""
        for position in order.cartposition_set.all():
            positionsText += f"{position.product.name}\t{position.totalPrice} Грн\t{position.count} шт\n"

        sendmail(request.user.email, f"Ваше замовлення підтверджене!\n"
                                                  f"Id замовлення: {order.id}\n"
                                                  f"Сума до сплати: {order.price} Грн\n"
                                                  f"\n"
                                                  f"Товари в замовленні:\n"
                                                  f"\n"
                                                  f"{positionsText}")

        for position in order.cartposition_set.all():
            position.status = "order"
            position.save()

        order.status = "confirmed"
        order.save()

        return render(request, 'orders/thanks.html')
    else:
        return HttpResponse("Bad request!")


@login_required
def cancel(request):
    if request.method == "POST":
        order = Order.objects.get(id=request.POST["id"])
        for position in order.cartposition_set.all():
            position.status = "cart"
            position.save()
        order.delete()
        return redirect("/cart")
    else:
        return HttpResponse("Bad request!")


@login_required()
def create(request):
    if request.method == "POST":

        ids = request.POST.getlist('id')
        counters = request.POST.getlist('counter')
        order = Order()
        order.user = auth.get_user(request)
        price = decimal.Decimal()
        order.save()

        for i in range(len(ids)):
            cartPosition = CartPosition.objects.get(id=ids[i])
            count = counters[i]
            cartPosition.count = count

            print(f"count: {count}")
            print(f"cartPosition.product.price: {cartPosition.product.price}")

            totalPrice = decimal.Decimal(count) * cartPosition.product.price
            cartPosition.totalPrice = totalPrice
            cartPosition.save()
            order.cartposition_set.add(cartPosition)
            cartPosition.save()
            price += totalPrice

        order.price = price
        order.status = "created"
        order.save()

        return redirect(f"check/{order.id}")
    else:
        return redirect(f"/cart")
