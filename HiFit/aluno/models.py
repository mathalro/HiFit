from __future__ import unicode_literals

import enum

from django.db import models
from utils.tipos import CaracteristicaQualitativa, ValorCaracteristica, tipoCaracteristica
from django.contrib.auth.models import User


class Caracteristica(models.Model):
    descricao = models.CharField(max_length=90)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super(Caracteristica, self).__init__(*args, **kwargs)
        if self.descricao == 'Não há':
            self.valor = ValorCaracteristica.NAO_HA.value
            self.tipo = tipoCaracteristica.NAO_HA.value
        elif self.descricao in CaracteristicaQualitativa.DOENCA:
            self.valor = ValorCaracteristica.DOENCA.value
            self.tipo = tipoCaracteristica.DOENCA.value
        elif self.descricao in CaracteristicaQualitativa.DIFICULDADE_MOTORA:
            self.valor = ValorCaracteristica.DIFICULDADE_MOTORA.value
            self.tipo = tipoCaracteristica.DIFICULDADE_MOTORA.value
        elif self.descricao in CaracteristicaQualitativa.PREFERENCIA:
            self.valor = ValorCaracteristica.PREFERENCIA.value
            self.tipo = tipoCaracteristica.PREFERENCIA.value
        elif self.descricao in CaracteristicaQualitativa.MALEFICIO:
            self.valor = ValorCaracteristica.MALEFICIO.value
            self.tipo = tipoCaracteristica.MALEFICIO.value

    def __str__(self):
        return str(self.descricao)


class Recomendacao(models.Model):
    data = models.DateField()  # Field name made lowercase.
    classificacao = models.ForeignKey('usuario.Classificacao', on_delete=models.CASCADE)  # Field name made lowercase.
    atividade = models.ForeignKey('usuario.Atividade',on_delete=models.CASCADE)
    aluno = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='recomendacoes_aluno', null=True)  # Field name made lowercase.
    instrutor = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='recomendacoes_instrutor', null=True)  # Field name made lowercase.
    regras = models.ManyToManyField('instrutor.Regra', related_name='recomendacoes')

    def __str__(self):
        return str("Aluno: " + str(self.aluno) + "- Instrutor: " + str(self.instrutor) + ", Classificacao: " + str(self.classificacao))

