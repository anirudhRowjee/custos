from django.contrib import admin
from django.urls import path, include

# importing the views
from . import views


urlpatterns = [
    path("", views.itemsview, name="home"),
    # the endpoint below is an API endpoint, and is for internal use only
    path("useritems/<int:id>", views.items),
]
