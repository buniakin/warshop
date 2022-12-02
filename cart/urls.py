from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('addToCart', addToCart),
    path('save', save),
    path('remove/<str:id>', remove),
    path('getCount', getCount)
]
