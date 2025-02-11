from rest_framework import viewsets
from .models import Proveedor, FacturaProveedor
from .serializers import ProveedorSerializer, FacturaProveedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    """
    API para gestionar proveedores
    """
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class FacturaProveedorViewSet(viewsets.ModelViewSet):
    """
    API para gestionar facturas de proveedores
    """
    queryset = FacturaProveedor.objects.all()
    serializer_class = FacturaProveedorSerializer
