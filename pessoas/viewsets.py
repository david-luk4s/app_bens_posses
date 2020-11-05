from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import PessoaSerializer


class PessoasViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = PessoaSerializer