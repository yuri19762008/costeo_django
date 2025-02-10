from django.db import models
from django.utils.timezone import now

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)  # 🔹 Se usa un valor por defecto
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class FacturaProveedor(models.Model):
    proveedor = models.ForeignKey("Proveedor", on_delete=models.CASCADE)
    fecha_emision = models.DateField(default=now)  # Se asigna una fecha por defecto
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=now)  # 🔹 Se usa default en lugar de auto_now_add
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_factura(self):
        return sum(item.precio_unitario * item.cantidad for item in self.detalles.all())

    def save(self, *args, **kwargs):
        self.total = self.get_total_factura()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura {self.id} - {self.proveedor.nombre} ({self.fecha_emision})"
