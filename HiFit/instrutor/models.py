from django.db import models



from django.contrib.auth.models import User

class Profissao(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Regra(models.Model):
    dono = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name="minhas_regras")
    solicitante = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, null=True, blank=True, related_name="regras_solicitadas")
    pontuacao = models.IntegerField()
    restricao = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE, related_name="restricao", null=True, blank=True)
    beneficio = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE, related_name="beneficio", null=True, blank=True)
    maleficio = models.ForeignKey('aluno.Caracteristica', on_delete=models.CASCADE, related_name="maleficio", null=True, blank=True)
    datacriacao = models.DateField(auto_now_add=True)  # Field name made lowercase.
    atividade = models.ForeignKey('usuario.Atividade', on_delete=models.CASCADE)  # Field name made lowercase.
    data_solicitacao = models.DateField(blank=True,null=True)
    def __str__(self):
        return str("Dono: " + str(self.dono) + ", " + str(self.atividade) + ", data de criacao: " + str(self.datacriacao))