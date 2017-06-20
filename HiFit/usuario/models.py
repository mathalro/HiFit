from django.db import models
from utils.tipos import TIPO, TIPOS_IDENTIFICACAO
# from instrutor.models import *
# from aluno.models import *

from django.contrib.auth.models import User


class Atividade(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

class Classificacao(models.Model):
    somanota = models.FloatField(blank=True,null=True)  # Field name made lowercase.
    somapessoas = models.IntegerField(blank=True,null=True)  # Field name made lowercase.

    def __str__(self):
        return str("Nota: " + str(self.somanota) + " Total: " + str(self.somapessoas))



class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_usuario = models.IntegerField()  # Field name made lowercase.
    datanascimento = models.CharField(max_length=10, null=True)  # Field name made lowercase.
    telefone = models.CharField(max_length=20)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    cpf = models.CharField(max_length=20)
    tipo_identificacao = models.CharField(max_length=5, choices=TIPOS_IDENTIFICACAO, default="CRM")
    identificacao = models.CharField(max_length=45, null=True)
    profissao = models.ForeignKey('instrutor.Profissao', on_delete=models.CASCADE, related_name='usuarios', null=True)  # Field name made lowercase.
    caracteristicas = models.ManyToManyField('aluno.Caracteristica',blank=True)
    nome = models.CharField(max_length=100, null=True)
    descricao = models.TextField(null=True)
    auth_id = models.CharField(max_length=32, null=True)
    situacao = models.IntegerField(null=True)    
    seguindo = models.ManyToManyField('Usuario', related_name='seguidores', blank=True)
    associado = models.ManyToManyField('Usuario', related_name='associados', blank=True)
    cadastro_completo = models.IntegerField(default=1)

    def isAluno(self):
        return self.tipo_usuario == TIPO['ALUNO']

    def __str__(self):
        return str(self.nome)

class AvaliacaoUsuario(models.Model):
    dono_avaliacao = models.ForeignKey(Usuario, related_name="dono",on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Usuario, related_name="avaliador",on_delete=models.CASCADE)
    nota = models.FloatField()

class Post(models.Model):
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')  # Field name made lowercase.
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)  # Field name made lowercase.
    privacidade = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class Comentario(models.Model):
    conteudo = models.TextField(max_length=140)
    data = models.DateField(auto_now=False, auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return str(self.data + ': ' +self.conteudo)


class Denuncia(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='denuncias')  # Field name made lowercase.

    def __str__(self):
        return str(self.titulo)


class Mensagem(models.Model):
    conteudo = models.TextField(max_length=140)
    data = models.DateField(auto_now_add=True)
    remetente = models.ForeignKey(Usuario, related_name='remetente')  # Field name made lowercase.
    destinatario = models.ForeignKey(Usuario, related_name='destinatario')  # Field name made lowercase.    


class Sugestao(models.Model):
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)