from django.contrib import admin
from django.urls import path,include

# importing the views
from . import views


urlpatterns = [
    path('', views.lists)
]
