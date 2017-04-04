# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Atividade(models.Model):
    nome = models.CharField(max_length=45)

    def __unicode__(self):
        return self.nome


class Caracteristica(models.Model):
    descricao = models.CharField(max_length=90)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return self.descricao
    

# class Caracteristicaaluno(models.Model):
#     caracteristica_idcaracteristica = models.ForeignKey(Caracteristica, models.DO_NOTHING, db_column='Caracteristica_idCaracteristica')  # Field name made lowercase.
#     usuario_login = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_login')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CaracteristicaAluno'
#         unique_together = (('caracteristica_idcaracteristica', 'usuario_login'),)


class Classificacao(models.Model):
    somanota = models.IntegerField(db_column='somaNota')  # Field name made lowercase.
    somapessoas = models.IntegerField(db_column='somaPessoas')  # Field name made lowercase.


class Comentario(models.Model):
    conteudo = models.TextField()
    data = models.DateField(auto_now=False, auto_now_add=True)
    post_idpost = models.ForeignKey('Post', models.DO_NOTHING, db_column='Post_idPost')  # Field name made lowercase.

    def __unicode__(self):
        return self.conteudo


class Denuncia(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='denuncias')  # Field name made lowercase.

    def __unicode__(self):
        return self.titulo


class Mensagem(models.Model):
    conteudo = models.TextField()
    data = models.DateField(auto_now_add=True)
    remetente = models.ForeignKey('Usuario', related_name='mensagens')  # Field name made lowercase.
    destinatario = models.ForeignKey('Usuario', related_name='mensagens')  # Field name made lowercase.    


class Post(models.Model):
    conteudo = models.TextField()
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='posts')  # Field name made lowercase.
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE, related_name='classificacao')  # Field name made lowercase.


class Profissao(models.Model):
    nome = models.CharField(max_length=100)

    __unicode__(self):
        return nome


class Recomendacao(models.Model):
    data = models.DateField(auto_now_add=True)  # Field name made lowercase.
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE, related_name='classificacao')  # Field name made lowercase.
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='recomendacoes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recomendacao'
        unique_together = (('regra_idregra', 'usuario_login'),)


class Regra(models.Model):
    idregra = models.IntegerField(db_column='idRegra', primary_key=True)  # Field name made lowercase.
    pontuacao = models.IntegerField(blank=True, null=True)
    restricao = models.ForeignKey(Caracteristica, models.DO_NOTHING, db_column='restricao', blank=True, null=True)
    beneficios = models.ForeignKey(Caracteristica, models.DO_NOTHING, db_column='beneficios', blank=True, null=True)
    maleficios = models.ForeignKey(Caracteristica, models.DO_NOTHING, db_column='maleficios', blank=True, null=True)
    datacriacao = models.DateField(db_column='dataCriacao', blank=True, null=True)  # Field name made lowercase.
    atividade_idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Regra'


class Sugestao(models.Model):
    idsugestao = models.IntegerField(db_column='idSugestao', primary_key=True)  # Field name made lowercase.
    conteudo = models.CharField(max_length=45, blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sugestao'


class Usuario(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    tipousuario = models.IntegerField(db_column='tipoUsuario')  # Field name made lowercase.
    senha = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    datanascimento = models.DateField(db_column='dataNascimento')  # Field name made lowercase.
    telefone = models.CharField(max_length=45, blank=True, null=True)
    classificacaopessoa_idclassificacao = models.ForeignKey(Classificacaopessoa, models.DO_NOTHING, db_column='ClassificacaoPessoa_idClassificacao')  # Field name made lowercase.
    cpf = models.CharField(max_length=45)
    identificacao = models.CharField(max_length=45, blank=True, null=True)
    profissao_idprofissao1 = models.ForeignKey(Profissao, models.DO_NOTHING, db_column='Profissao_idProfissao1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'
