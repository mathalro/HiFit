from django.db import models



from django.contrib.auth.models import User
# from usuario.models import *
# from aluno.models import *

class Profissao(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Regra(models.Model):
    dono = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    restricao = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE, related_name="restricao", null=True, blank=True)
    beneficio = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE, related_name="beneficio", null=True, blank=True)
    maleficio = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE, related_name="maleficio", null=True, blank=True)
    datacriacao = models.DateField(auto_now_add=True)  # Field name made lowercase.
    atividade = models.ForeignKey('usuario.Atividade', on_delete=models.CASCADE)  # Field name made lowercase.