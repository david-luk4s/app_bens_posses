from django.shortcuts import get_object_or_404
from rest_framework import serializers
from pessoas.models import User
from .models import Empresas
from pessoas.serializers import PessoaSerializer
from pycpfcnpj import cpf, cnpj


class DonoEmpresaSerializer(serializers.ModelSerializer):
    data_abertura = serializers.DateField(input_formats=['%d/%m/%Y'], format='%d/%m/%Y')

    class Meta:
        model = Empresas
        fields = ('id', 'cnpj', 'razao_social', 'telefone', 'data_abertura', 'dono_pessoa', 'dono_empresa')


class EmpresasSerializer(serializers.ModelSerializer):
    data_abertura = serializers.DateField(input_formats=['%d/%m/%Y'], format='%d/%m/%Y')

    # Retorna apenas CPF da Pessoa Dona
    dono_pessoa = serializers.CharField(required=False)
    # Retorna todos os dados da Pessoa Dona
    # dono_pessoa = PessoaSerializer(allow_null=True, required=False) # Test not coverage

    # Retorna apenas CNPJ da Empresa Dona
    dono_empresa = serializers.CharField(required=False)
    # Retorna todos os dados da Empresa Dona
    #dono_empresa = DonoEmpresaSerializer(allow_null=True, required=False) # Test not coverage
    cpf_or_cnpj = serializers.CharField(required=False)


    def create(self, validated_data):
        cpf_or_cnpj = validated_data.get('cpf_or_cnpj', False)

        if not cpf_or_cnpj:
            data =  Empresas.objects.create(**validated_data)

        elif cpf.validate(cpf_or_cnpj):
            instance = get_object_or_404(User, cpf=cpf_or_cnpj) # Instance Pessoa
            del validated_data['cpf_or_cnpj']
            data =  Empresas.objects.create(**validated_data, dono_pessoa=instance)
            
        elif cnpj.validate(cpf_or_cnpj):
            instance = get_object_or_404(Empresas, cnpj=cpf_or_cnpj) # Instance Empresa
            del validated_data['cpf_or_cnpj']
            data =  Empresas.objects.create(**validated_data, dono_empresa=instance)
        
        return data

    class Meta:
        model = Empresas
        fields = ('id', 'cnpj', 'razao_social', 'telefone', 'data_abertura', 'dono_pessoa', 'dono_empresa', 'cpf_or_cnpj')

