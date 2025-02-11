from rest_framework import serializers
from .models import Receta, DetalleReceta

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'  # Devuelve todos los campos en JSON

class DetalleRecetaSerializer(serializers.ModelSerializer):
    receta = RecetaSerializer(read_only=True)  # Muestra la información de la receta
    producto = serializers.StringRelatedField()  # Muestra solo el nombre del producto

    class Meta:
        model = DetalleReceta
        fields = '__all__'
