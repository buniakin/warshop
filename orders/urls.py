from django.urls import re_path, path
from .views import *

urlpatterns = [
    path("create", create),
    path("check/<int:id>", check),
    path("id/<int:id>", order),
    path("cancel", cancel),
    path("confirm", confirm),
    path("index", index),
]
