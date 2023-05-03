from django.shortcuts import render

from .models import *


# Create your views here.

def home_screen_view(request):
    news = New.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()
    return render(request, 'Inicio.html', context={'new': news, 'authors': authors, 'categories': categories})


def novedades_screen_view(request):
    return render(request, 'Novedades.html')


def centro_estudiantes_screen_view(request):
    return render(request, 'Centro-Estudiantes.html')


def deportes_screen_view(request):
    return render(request, 'Deportes.html')
