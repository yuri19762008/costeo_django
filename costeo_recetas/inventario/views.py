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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre', 'unidad_medida']
    search_fields = ['nombre']
    ordering_fields = ['nombre', 'stock_actual', 'precio_actual']  # Permite ordenar por estos campos
    ordering = ['nombre']  # Orden predeterminado: alfabético por nombre

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    """
    API para gestionar detalles de facturas
    """
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer







