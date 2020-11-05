from django.db import models
from django.contrib.auth import get_user_model


class BensPosses(models.Model):
    bens = models.TextField(verbose_name='Bens', max_length=300, null=True, blank=True)
    posses = models.TextField(verbose_name='Posses', max_length=300, null=True, blank=True)
    responsavel = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.responsavel

    class Meta:
        verbose_name = 'Bens e Posse'
        verbose_name_plural = 'Bens e Posses'