from rest_framework.viewsets import ModelViewSet
from .models import Empresas
from .serializers import EmpresasSerializer


class EmpresaViewSets(ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

