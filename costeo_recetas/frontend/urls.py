from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='frontend-index'),
    path('proveedores/', views.proveedores, name='frontend-proveedores'),
    path('productos/', views.productos, name='frontend-productos'),
    path('recetas/', views.recetas, name='frontend-recetas'),
]
