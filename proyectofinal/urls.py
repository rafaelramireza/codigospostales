from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar_por_codigo_postal/', views.buscar_por_codigo_postal, name='buscar_por_codigo_postal'),
    path('buscar_por_asentamiento/', views.buscar_por_asentamiento, name='buscar_por_asentamiento'),
    path('buscar_por_municipio/', views.buscar_por_municipio, name='buscar_por_municipio'),
    path('buscar_por_estado/', views.buscar_por_estado, name='buscar_por_estado'),
    path('get_municipios_by_estado/', views.get_municipios_by_estado, name='get_municipios_by_estado'),
    path('get_asentamientos_by_municipio/', views.get_asentamientos_by_municipio, name='get_asentamientos_by_municipio'),
    path('buscar_por_estado_municipio_asentamiento/', views.buscar_por_estado_municipio_asentamiento, name='buscar_por_estado_municipio_asentamiento'),
    path('buscar_por_codigo_postal/', views.buscar_por_codigo_postal, name='buscar_por_codigo_postal'),
]
