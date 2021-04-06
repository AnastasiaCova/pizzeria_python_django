from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name = 'main'),
    path('aboutus', views.AboutUs, name = 'aboutus'),
    path('pizza', views.Pizza, name = 'pizza'),
    path('drinks', views.Drinks, name = 'drinks'),
]
