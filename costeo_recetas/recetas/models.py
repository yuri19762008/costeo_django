from django.db import models
from inventario.models import Producto

class Receta(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_costo_total(self):
        ingredientes = self.ingredientes.all()
        total = sum(ingrediente.costo_total for ingrediente in ingredientes) if ingredientes.exists() else 0
        self.costo_total = total
        self.save()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):  # Antes se llamaba DetalleReceta
    receta = models.ForeignKey(Receta, related_name="ingredientes", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.costo_total = self.cantidad * (self.producto.precio_actual or 0)
        super().save(*args, **kwargs)
        self.receta.calcular_costo_total()

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} unidades"
