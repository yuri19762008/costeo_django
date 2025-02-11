from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def proveedores(request):
    return render(request, 'frontend/proveedores.html')

def productos(request):
    return render(request, 'frontend/productos.html')

def recetas(request):
    return render(request, 'frontend/recetas.html')
