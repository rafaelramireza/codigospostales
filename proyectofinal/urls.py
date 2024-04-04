"""
URL configuration for proyectofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
from .views import buscar_por_estado_municipio_asentamiento

# Definición de las URL para las vistas de la aplicación

urlpatterns = [
    # URL para la página de inicio
    path('', views.index, name='index'),
    # URL para buscar por código postal
    path('buscar_por_codigo_postal/', views.buscar_por_codigo_postal, name='buscar_por_codigo_postal'),
    # URL para buscar por asentamiento
    path('buscar_por_asentamiento/', views.buscar_por_asentamiento, name='buscar_por_asentamiento'),
    # URL para buscar por municipio
    path('buscar_por_municipio/', views.buscar_por_municipio, name='buscar_por_municipio'),
    # URL para buscar por estado
    path('buscar_por_estado/', views.buscar_por_estado, name='buscar_por_estado'),
    # URL para obtener municipios por estado
    path('get_municipios_by_estado/', views.get_municipios_by_estado, name='get_municipios_by_estado'),
    # URL para obtener asentamientos por municipio
    path('get_asentamientos_by_municipio/', views.get_asentamientos_by_municipio, name='get_asentamientos_by_municipio'),
    # URL para buscar por estado, municipio y asentamiento
    path('buscar_por_estado_municipio_asentamiento/', views.buscar_por_estado_municipio_asentamiento, name='buscar_por_estado_municipio_asentamiento'),
]
