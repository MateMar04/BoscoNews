"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from confApp.views import home_screen_view, novedades_screen_view, centro_estudiantes_screen_view, deportes_screen_view, \
    new_screen_view
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('novedades/', novedades_screen_view, name='novedades'),
    path('centro-estudiantes/', centro_estudiantes_screen_view, name='centro-estudiantes'),
    path('deportes/', deportes_screen_view, name='deportes'),
    path('news/<int:new_id>', new_screen_view, name='new')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
