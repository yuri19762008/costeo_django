from rest_framework import viewsets, filters
from .models import Receta, Ingrediente
from .serializers import RecetaSerializer, IngredienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.http import HttpResponse
from rest_framework import serializers
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import render


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    
class IngredienteViewSet(viewsets.ModelViewSet):  # Antes era DetalleRecetaViewSet
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class RecetaSerializer(serializers.ModelSerializer):
    costo_total = serializers.SerializerMethodField()  # Agregamos un campo calculado

    class Meta:
        model = Receta
        fields = '__all__'

    def get_costo_total(self, obj):
        return sum(ingrediente.cantidad * ingrediente.producto.precio_actual for ingrediente in obj.ingredientes.all())

class ReporteCosteoRecetas(APIView):
    """
    Endpoint para generar un reporte de costeo de recetas.
    Devuelve un JSON con los costos detallados y permite exportar a Excel.
    """

    def get(self, request, *args, **kwargs):
        # Obtener todas las recetas
        recetas = Receta.objects.all()

        # Estructurar los datos para el reporte
        data = []
        for receta in recetas:
            total_costo = sum(
                ingrediente.cantidad * ingrediente.producto.precio_actual
                for ingrediente in receta.ingredientes.all()
            )
            ingredientes = [
                f"{detalle.producto.nombre} ({detalle.cantidad} {detalle.producto.unidad_medida})"
                for detalle in receta.ingredientes.all()
            ]
            data.append({
                "id": receta.id,
                "nombre": receta.nombre,
                "descripcion": receta.descripcion,
                "costo_total": total_costo,
                "ingredientes": ", ".join(ingredientes),
            })

        # Verificar si el usuario quiere exportar a Excel
        if request.GET.get("export") == "excel":
            return self.exportar_excel(data)
        elif request.GET.get("export") == "pdf":
            return self.exportar_pdf(data)

        return Response(data, status=status.HTTP_200_OK)

    def exportar_excel(self, data):
        """Genera un archivo Excel con los datos del reporte"""
        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte_costeo.xlsx"'
        df.to_excel(response, index=False)
        return response
    
    def exportar_pdf(self, data):
        """Genera un archivo PDF con los datos del reporte"""
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte_costeo.pdf"'
        pdf = canvas.Canvas(response, pagesize=letter)
        pdf.drawString(100, 750, "Reporte de Costeo de Recetas")

        y = 730
        for item in data:
            pdf.drawString(100, y, f"Receta: {item['nombre']} - Costo: ${item['costo_total']}")
            y -= 20
            pdf.drawString(120, y, f"Ingredientes: {item['ingredientes']}")
            y -= 30

        pdf.showPage()
        pdf.save()
        return response

import json

def lista_recetas(request):
    recetas = Receta.objects.all()
    for receta in recetas:
        try:
            receta.ingredientes = json.loads(receta.ingredientes)  # Convertir string JSON a lista Python
        except:
            receta.ingredientes = []  # Si hay un error, asignar lista vacía

    return render(request, "recetas.html", {"recetas": recetas})
