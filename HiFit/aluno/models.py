from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User


class Caracteristica(models.Model):
    descricao = models.CharField(max_length=90)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo = models.IntegerField()

    def __unicode__(self):
        return self.descricao
    

class Recomendacao(models.Model):
    data = models.DateField(auto_now_add=True)  # Field name made lowercase.
    classificacao = models.ForeignKey('usuario.Classificacao', on_delete=models.CASCADE)  # Field name made lowercase.
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='recomendacoes')  # Field name made lowercase.
    regras = models.ManyToManyField('instrutor.Regra', related_name='recomendacoes')
