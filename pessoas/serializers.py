from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class PessoaSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'cpf', 'number', 'username', 'first_name', 'last_name')