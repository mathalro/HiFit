from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Atividade)
admin.site.register(Classificacao)
admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Denuncia)
admin.site.register(Mensagem)
admin.site.register(Sugestao)
admin.site.register(AvaliacaoUsuario)