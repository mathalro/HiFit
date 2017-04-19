from django.shortcuts import render

from usuario.models import Usuario
from .models import Regra
from usuario.models import Atividade
from aluno.models import Caracteristica
from utils.tipos import tipoCaracteristica
from django.db.models import Q      # Para fazer WHERE x=a and x=b
from django.contrib.auth import get_user


# Create your views here.
# Tela de Regras
def regras(request):
    atividades = Atividade.objects.all()
    restricoes = Caracteristica.objects.filter(tipo=tipoCaracteristica.FISIOLOGICA)
    beneficios = Caracteristica.objects.filter(Q(tipo=tipoCaracteristica.FISIOLOGICA) | Q(tipo=tipoCaracteristica.PREFERENCIA))
    maleficios = Caracteristica.objects.filter(Q(tipo=tipoCaracteristica.FISIOLOGICA) | Q(tipo=tipoCaracteristica.PREFERENCIA))
    usuario_logado = Usuario.objects.get(user=get_user(request))

    if request.method == 'POST':  # if the form has been filled
        atividade = request.POST['sel1_cad_atividade']
        restricao = request.POST['sel1_cad_restricao']
        beneficio = request.POST['sel1_cad_beneficio']
        maleficio = request.POST['sel1_cad_maleficio']
        pontuacao = request.POST['in_cad_pontuacao']
        # creating an user object containing all the data
        regra_obj = Regra(atividade=Atividade.objects.get(nome=atividade),
                          restricao=Caracteristica.objects.get(descricao=restricao),
                          beneficios=Caracteristica.objects.get(descricao=beneficio),
                          maleficios=Caracteristica.objects.get(descricao=maleficio),
                          pontuacao=pontuacao,
                          dono=Usuario.objects.get(user=usuario_logado.user))
        # saving all the data in the current object into the database
        regra_obj.save()

    minhas_regras = Regra.objects.filter(dono=usuario_logado)
    outras_regras = Regra.objects.exclude(dono=usuario_logado)
    return render(request, 'regras.html', {'atividades': atividades,
                                           'restricoes': restricoes,
                                           'beneficios': beneficios,
                                           'maleficios': maleficios,
                                           'minhas_regras': minhas_regras,
                                           'outras_regras': outras_regras})