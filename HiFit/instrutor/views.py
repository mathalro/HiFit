from django.shortcuts import render
from usuario.models import Atividade
from aluno.models import Caracteristica

# Create your views here.
# Tela de Regras
def regras(request):
    atividades = Atividade.objects.all()
    restricoes = Caracteristica.objects.filter()
    return render(request,'regras.html', {"atividades": atividades})
