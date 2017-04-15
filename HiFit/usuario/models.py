from django.db import models

# from instrutor.models import *
# from aluno.models import *

from django.contrib.auth.models import User


class Atividade(models.Model):
    nome = models.CharField(max_length=45)

    def __unicode__(self):
        return self.nome
    

class Classificacao(models.Model):
    somanota = models.IntegerField()  # Field name made lowercase.
    somapessoas = models.IntegerField()  # Field name made lowercase.

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_usuario = models.IntegerField()  # Field name made lowercase.
    nome = models.CharField(max_length=100)
    datanascimento = models.DateField()  # Field name made lowercase.
    telefone = models.CharField(max_length=20)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE,blank=True,null=True)  # Field name made lowercase.
    cpf = models.CharField(max_length=20)
    identificacao = models.CharField(max_length=45)
    profissao = models.ForeignKey('instrutor.Profissao', on_delete=models.CASCADE, related_name='usuarios')  # Field name made lowercase.
    caracteristicas = models.ManyToManyField('aluno.Caracteristica',blank=True)

    def __str__(self):
        return self.nome

class Post(models.Model):
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')  # Field name made lowercase.
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)  # Field name made lowercase.


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
    remetente = models.ForeignKey(Usuario, related_name='remetente')  # Field name made lowercase.
    destinatario = models.ForeignKey(Usuario, related_name='destinatario')  # Field name made lowercase.    


class Sugestao(models.Model):
    conteudo = models.TextField(max_length=500)
    data = models.DateField(auto_now_add=True)


