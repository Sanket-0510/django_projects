
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index2", views.index2, name="index2"),
    path("counter", views.counter, name="counter"),
    path("register", views.register, name= "register"),
    path("login", views.login, name= "login")

]