from django.shortcuts import render
from django.views import View


def Main(request):
    return render(request, 'main/main.html')


def AboutUs(request):
    return render(request, 'main/aboutus.html')


def Pizza(request):
    return render(request, 'main/pizza.html')


def ProductCard(request):
    return render(request, 'main/productcard.html')


def Drinks(request):
    return render(request, 'main/drinks.html')


def Snacks(request):
    return render(request, 'main/snacks.html')

