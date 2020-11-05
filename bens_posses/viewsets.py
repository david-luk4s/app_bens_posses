from rest_framework import viewsets
from .serializers import BensPossesSerializer
from .models import BensPosses


class BensPossesViewSet(viewsets.ModelViewSet):
    queryset = BensPosses.objects.all()
    serializer_class = BensPossesSerializer

    
