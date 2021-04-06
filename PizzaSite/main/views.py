from django.shortcuts import render
from django.views import View
from .models import MyNews


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


def Sales(request):
    return render(request, 'main/sales.html')


def News(request):
    return render(request, 'main/news.html')


class NewsCard(View):
    def get(self, request, pk):
        news = MyNews.objects.filter(pk=pk)
        return render(request, 'main/newscard.html', {"news": news})

