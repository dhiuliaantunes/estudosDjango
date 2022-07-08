from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Categoria
from core.serializer import CategoriaSerializer

#CRUD COMPLETO COM GENERIC VIEW
class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailsGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field ='id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer