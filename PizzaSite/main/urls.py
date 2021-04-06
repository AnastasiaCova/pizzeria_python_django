from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name = 'main'),
    path('aboutus', views.AboutUs, name = 'aboutus'),
]
