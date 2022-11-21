"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from project.views import contextoEncuentrosJugados,contadoresAdmin, contextoJugador, contextoCompetencias,contextoEquipo,contextoCompetenciasFutbol,contextoContacto,contextoFixtureCompetencia,index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', contadoresAdmin), 
    path('admin/', admin.site.urls),
    path('jugador/<str:alias>', contextoJugador), 
    path('equipo/<str:nombre_equipo>', contextoEquipo),
    path('competencias/<str:nombre_deporte>', contextoCompetencias),
    path('competencias/futbol/<str:nombre_competicion>', contextoCompetenciasFutbol),
    path('contacto', contextoContacto),
    path('competencias/<str:nombre_competicion>/fixture',contextoFixtureCompetencia),
    path('competencias/<str:nombre_competicion>/encuentros',contextoEncuentrosJugados),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)