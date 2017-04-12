from django.db import models



from django.contrib.auth.models import User
# from usuario.models import *
# from aluno.models import *

class Profissao(models.Model):
    nome = models.CharField(max_length=40)

    def __unicode__(self):
        return nome


class Regra(models.Model):
    dono = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    restricao = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE)
    beneficios = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE)
    maleficios = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE)
    datacriacao = models.DateField(auto_now_add=True)  # Field name made lowercase.
    atividade = models.ForeignKey('usuario.Atividade', on_delete=models.CASCADE)  # Field name made lowercase.

