"""
URL configuration for costeo_recetas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from proveedores.views import ProveedorViewSet, FacturaProveedorViewSet
from inventario.views import ProductoViewSet, DetalleFacturaViewSet
from recetas.views import RecetaViewSet, DetalleRecetaViewSet

# Definir el router de DRF
router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'facturas', FacturaProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'detalle-facturas', DetalleFacturaViewSet)
router.register(r'recetas', RecetaViewSet)
router.register(r'detalle-recetas', DetalleRecetaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Incluye todas las rutas de los modelos registrados con ViewSets
    path('api/', include('recetas.urls')),  # 🔹 Agregar esta línea para incluir las rutas de la app recetas
]
