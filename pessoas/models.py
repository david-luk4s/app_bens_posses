from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True)
    number = models.CharField(verbose_name='Número', max_length=14, null=True, blank=True)

    def __str__(self):
        return self.cpf