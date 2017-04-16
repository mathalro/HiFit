from django.shortcuts import render
from usuario.models import Atividade
from aluno.models import Caracteristica
from usuario.models import Usuario
from .models import Regra
from django.db.models import Q      # Para fazer WHERE x=a and x=b
from .forms import regrasCadastroForm
from django.forms.forms import BoundField
from django.contrib.auth import get_user


# Create your views here.
# Tela de Regras
def regras(request):
    usuario_logado = Usuario.objects.get(user=get_user(request))
    minhas_regras = Regra.objects.filter(dono=usuario_logado)
    outras_regras = Regra.objects.exclude(dono=usuario_logado)
    if request.method == 'POST':  # if the form has been filled
        atividade = request.POST.get('atividade', '')
        restricao = request.POST.get('restricao', '')
        beneficio = request.POST.get('beneficio', '')
        maleficio = request.POST.get('maleficio', '')
        pontuacao = request.POST.get('pontuacao', '')
        # creating an user object containing all the data
        regra_obj = Regra(atividade=Atividade.objects.get(nome=atividade),
                          restricao=Caracteristica.objects.get(descricao=restricao),
                          beneficios=Caracteristica.objects.get(descricao=beneficio),
                          maleficios=Caracteristica.objects.get(descricao=maleficio),
                          pontuacao=pontuacao,
                          dono=Usuario.objects.get(user=usuario_logado))
        # saving all the data in the current object into the database
        regra_obj.save()
        return render(request, 'regras.html',
                      {'regra_obj': regra_obj, 'is_registered': True})  # Redirect after POST

    form = regrasCadastroForm()  # an unboundform
    return render(request, 'regras.html', {'form': form, 'minhas_regras': minhas_regras, 'outras_regras': outras_regras})