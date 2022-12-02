from django.http import request, response

from warshop.settings import CART_SESSION_KEY


def CheckCookie():
    key = request.session.session_key
    if (key is None):
        request.session.create()
        key = request.session.session_key

    cookie = request.COOKIES.get(CART_SESSION_KEY)
    if (cookie is None):
        response.cookies[CART_SESSION_KEY] = key