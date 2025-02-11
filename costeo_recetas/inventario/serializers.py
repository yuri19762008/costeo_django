from rest_framework import serializers
from .models import Producto, DetalleFactura

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  # Devuelve todos los campos en JSON

class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)  # Muestra los datos del producto

    class Meta:
        model = DetalleFactura
        fields = '__all__'
