from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name = 'main'),
    path('aboutus', views.AboutUs, name = 'aboutus'),
    path('pizza', views.Pizza, name = 'pizza'),
    path('productcard', views.ProductCard, name = 'productcard'),
    path('drinks', views.Drinks, name = 'drinks'),
    path('snacks', views.Snacks, name = 'snacks'),
    path('sales', views.Sales, name = 'sales'),
]
