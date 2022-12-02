from django.urls import path
from . import views
from .views import profile


urlpatterns = [
    path("signup/", views.signup.as_view(), name="signup"),
    path('profile', profile)
]
