from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recetas.views import RecetaViewSet, IngredienteViewSet

router = DefaultRouter()
router.register(r'recetas', RecetaViewSet)
router.register(r'ingredientes', IngredienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

