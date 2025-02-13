from django.contrib import admin
from recetas.models import Receta, Ingrediente  # Importamos los modelos correctos

# Configuración del Admin para el modelo Ingrediente
class IngredienteInline(admin.TabularInline):
    model = Ingrediente  # Permite gestionar ingredientes dentro de la receta
    extra = 1  # Muestra un campo vacío adicional para agregar ingredientes rápidamente

# Configuración del Admin para el modelo Receta
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'costo_total')  # Muestra estos campos en la lista de recetas
    search_fields = ('nombre',)  # Permite buscar recetas por nombre
    inlines = [IngredienteInline]  # Permite agregar ingredientes desde la receta

# Configuración del Admin para Ingredientes (Opcional)
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'receta', 'producto', 'cantidad', 'costo_total')
    search_fields = ('receta__nombre', 'producto__nombre')  # Buscar ingredientes por receta o producto
