from rest_framework import serializers
from .models import Proveedor, FacturaProveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'  # Devuelve todos los campos en JSON

class FacturaProveedorSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)  # Muestra los datos del proveedor

    class Meta:
        model = FacturaProveedor
        fields = '__all__'
