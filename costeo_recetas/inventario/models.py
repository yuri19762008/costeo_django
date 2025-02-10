from django.db import models
from proveedores.models import FacturaProveedor
from enum import Enum
from django.utils.timezone import now


class UnidadMedida(Enum):
    KG = 'kg'
    G = 'g'
    L = 'l'
    ML = 'ml'
    UNIDAD = 'unidad'

class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    unidad_medida = models.CharField(
        max_length=10,
        choices=[('kg', 'Kilogramo'), ('g', 'Gramo'), ('l', 'Litro'), ('ml', 'Mililitro'), ('unidad', 'Unidad')]
    )
    stock_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=now)  # 🔹 Se usa un valor por defecto
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.unidad_medida})"



class DetalleFactura(models.Model):
    factura = models.ForeignKey(FacturaProveedor, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now)  # <- Se define un valor predeterminado

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.producto.precio_actual != self.precio_unitario:
            self.producto.precio_actual = self.precio_unitario
            self.producto.save()

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad} x {self.precio_unitario}"


