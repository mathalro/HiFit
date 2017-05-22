from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User


import enum


class ValorCaracteristica(enum.Enum):
    PREFERENCIA = 0
    ALTURA = 1
    PESO = 3
    DOENCA = 5
    DIFICULDADE_MOTORA = 5


class CaracteristicaQualitativa():
    PREFERENCIA = ['Correção da postura', 'Ganho de massa muscular', 'Melhor condicionamento físico',
                   'Melhor flexibilidade', 'Melhor respiração', 'Perda de peso']
    DOENCA = ['Asma', 'Diabetes', 'Pressão alta']
    DIFICULDADE_MOTORA = ['Dor no joelho', 'Hérnia de disco', 'Mobilidade braço', 'Mobilidade perna']


class TipoCaracteristica(enum.Enum):
    PREFERENCIA = 0
    ALTURA = 1
    PESO = 2
    DOENCA = 3
    DIFICULDADE_MOTORA = 4


class Caracteristica(models.Model):
    descricao = models.CharField(max_length=90)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super(Caracteristica, self).__init__(*args, **kwargs)
        if self.descricao in CaracteristicaQualitativa.DOENCA:
            self.valor = ValorCaracteristica.DOENCA.value
            self.tipo = TipoCaracteristica.DOENCA.value
        elif self.descricao in CaracteristicaQualitativa.DIFICULDADE_MOTORA:
            self.valor = ValorCaracteristica.DIFICULDADE_MOTORA.value
            self.tipo = TipoCaracteristica.DIFICULDADE_MOTORA.value
        elif self.descricao in CaracteristicaQualitativa.PREFERENCIA:
            self.valor = ValorCaracteristica.PREFERENCIA.value
            self.tipo = TipoCaracteristica.PREFERENCIA.value

    def __str__(self):
        return str(self.descricao)


class Recomendacao(models.Model):
    data = models.DateField()  # Field name made lowercase.
    classificacao = models.ForeignKey('usuario.Classificacao', on_delete=models.CASCADE)  # Field name made lowercase.
    aluno = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='recomendacoes_aluno', null=True)  # Field name made lowercase.
    instrutor = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='recomendacoes_instrutor', null=True)  # Field name made lowercase.
    regras = models.ManyToManyField('instrutor.Regra', related_name='recomendacoes')

    def __str__(self):
        return "Aluno: " + str(self.aluno) + "- Instrutor: " + str(self.instrutor) + ", Classificacao: " + str(self.classificacao)

