from django.db import models
from django.contrib.auth import get_user_model


class Empresas(models.Model):
    cnpj = models.CharField(verbose_name='CNPJ', max_length=18, unique=True)
    razao_social = models.CharField(verbose_name='Razão Social', max_length=100)
    telefone = models.CharField(verbose_name='Telefone', max_length=15)
    data_abertura = models.DateField(verbose_name='Data de Abertura')
    dono_pessoa = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    dono_empresa = models.ForeignKey('Empresas', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.cnpj

    @property
    def cpf_or_cnpj(self):
        return self.cnpj