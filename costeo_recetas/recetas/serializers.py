from rest_framework import serializers
from recetas.models import Receta, Ingrediente
from inventario.models import Producto

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = Receta
        fields = ['id', 'nombre', 'descripcion', 'costo_total', 'ingredientes']


