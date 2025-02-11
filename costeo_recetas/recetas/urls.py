from django.urls import path
from .views import ReporteCosteoRecetas

urlpatterns = [
    path('reporte-costeo/', ReporteCosteoRecetas.as_view(), name='reporte-costeo'),
]
