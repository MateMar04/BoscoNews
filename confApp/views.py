from django.shortcuts import render


# Create your views here.

def home_screen_view(request):
    return render(request, 'Inicio.html')


def novedades_screen_view(request):
    return render(request, 'novedades.html')


def centro_estudiantes_screen_view(request):
    return render(request, 'Centro-Estudiantes.html')


def deportes_screen_view(request):
    return render(request, 'Deportes.html')
