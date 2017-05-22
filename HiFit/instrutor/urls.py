from django.conf.urls import url
from .views import *
urlpatterns = [
	url(r'^cadastro/',cadastroInstrutor),
	url(r'^regras/', regras),
	url(r'^meu_cadastro/',editarCadastro),
	url(r'^relatorios/',relatorios)
]