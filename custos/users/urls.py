from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('me', views.myaccount, name="myaccount"),
    path('login', views.loginview, name="login"),
    path('register', views.registerview, name="signup")
]
