from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializer import CategoriaSerializer

#CRUD COMPLETO COM MODELVIEWSETS
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer