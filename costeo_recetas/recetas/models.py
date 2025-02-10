from django.utils.timezone import now
from django.db import models
from inventario.models import Producto

class Receta(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)  # 🔹 Se usa un valor por defecto
    updated_at = models.DateTimeField(auto_now=True)

    def get_costo_total(self):
        return sum(ingrediente.cantidad * ingrediente.producto.precio_actual for ingrediente in self.ingredientes.all())

    def __str__(self):
        return self.nombre

class DetalleReceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name="ingredientes")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now)  # 🔹 Se usa default en lugar de auto_now_add

    def __str__(self):
        return f"{self.receta.nombre} - {self.cantidad} {self.producto.unidad_medida} de {self.producto.nombre}"
