from django.conf.urls import url
<<<<<<< HEAD
from .views import *
urlpatterns = [
	url(r'^cadastro/',cadastroInstrutor)
=======
from . import views

urlpatterns = [
    url(r'^regras', views.regras, name='regras'),
>>>>>>> origin/caminho
]