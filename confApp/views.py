from django.shortcuts import render

from .models import *


# Create your views here.

def home_screen_view(request):
    news = New.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request, 'Inicio.html',
                  context={'new': news, 'authors': authors, 'categories': categories, 'images': images})


def novedades_screen_view(request):
    category = Category.objects.get(id=3)
    news = New.objects.filter(category=category)
    authors = Author.objects.all()
    images = Image.objects.all()
    return render(request, 'Inicio.html',
                  context={'new': news, 'authors': authors, 'categories': category, 'images': images})


def centro_estudiantes_screen_view(request):
    category = Category.objects.get(id=1)
    news = New.objects.filter(category=category)
    authors = Author.objects.all()
    images = Image.objects.all()
    return render(request, 'Inicio.html',
                  context={'new': news, 'authors': authors, 'categories': category, 'images': images})


def deportes_screen_view(request):
    category = Category.objects.get(name='Deportes')
    news = New.objects.filter(category=category)
    authors = Author.objects.all()
    return render(request, 'Inicio.html', context={'new': news, 'authors': authors, 'categories': category})
