# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.auth.models import User


class Atividade(models.Model):
    nome = models.CharField(max_length=45)

    def __unicode__(self):
        return self.nome


class Caracteristica(models.Model):
    descricao = models.CharField(max_length=90)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo = models.IntegerField()

    def __unicode__(self):
        return self.descricao
    

class Classificacao(models.Model):
    somanota = models.IntegerField()  # Field name made lowercase.
    somapessoas = models.IntegerField()  # Field name made lowercase.


class Comentario(models.Model):
    conteudo = models.TextField(max_length=140)
    data = models.DateField(auto_now=False, auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Field name made lowercase.

    def __unicode__(self):
        return self.data + ': ' +self.conteudo


class Denuncia(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='denuncias')  # Field name made lowercase.

    def __unicode__(self):
        return self.titulo


class Mensagem(models.Model):
    conteudo = models.TextField(max_length=140)
    data = models.DateField(auto_now_add=True)
    remetente = models.ForeignKey(Usuario, related_name='mensagens')  # Field name made lowercase.
    destinatario = models.ForeignKey(Usuario, related_name='mensagens')  # Field name made lowercase.    


class Post(models.Model):
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')  # Field name made lowercase.
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)  # Field name made lowercase.

    
class Profissao(models.Model):
    nome = models.CharField(max_length=40)

    __unicode__(self):
        return nome


class Recomendacao(models.Model):
    data = models.DateField(auto_now_add=True)  # Field name made lowercase.
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)  # Field name made lowercase.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recomendacoes')  # Field name made lowercase.
    regras = models.ManyToManyField(Regra, on_delete=models.SET_NULL, 'recomendacoes')

class Regra(models.Model):
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    restricao = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    beneficios = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    maleficios = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    datacriacao = models.DateField(auto_now_add=True)  # Field name made lowercase.
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)  # Field name made lowercase.


class Sugestao(models.Model):
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)


class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_usuario = models.IntegerField()  # Field name made lowercase.
    datanascimento = models.DateField()  # Field name made lowercase.
    telefone = models.CharField(max_length=20)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)  # Field name made lowercase.
    cpf = models.CharField(max_length=20)
    identificacao = models.CharField(max_length=45)
    profissao = models.ForeignKey(Profissao, on_delete=models.CASCADE, related_name='usuarios')  # Field name made lowercase.
    caracteristicas = models.ManyToManyField(Caracteristica, on_delete=models.SET_NULL, null=True,blank=True)