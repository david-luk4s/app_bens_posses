from rest_framework import serializers
from .models import BensPosses


class BensPossesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BensPosses
        fields = ('id', 'bens', 'posses', 'responsavel')