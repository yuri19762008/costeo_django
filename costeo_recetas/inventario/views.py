from rest_framework import viewsets, filters
from .models import Producto, DetalleFactura
from .serializers import ProductoSerializer, DetalleFacturaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API para gestionar productos (ingredientes)
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nombre', 'unidad_medida']  # Permite filtrar por nombre y unidad de medida
    search_fields = ['nombre']  # Permite buscar productos por nombre

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    """
    API para gestionar detalles de facturas
    """
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer








