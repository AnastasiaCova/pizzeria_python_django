from django.shortcuts import render
from django.views import View


def Main(request):
    return render(request, 'main/main.html')


def AboutUs(request):
    return render(request, 'main/aboutus.html')


def Pizza(request):
    return render(request, 'main/pizza.html')


def Drinks(request):
    return render(request, 'main/drinks.html')


