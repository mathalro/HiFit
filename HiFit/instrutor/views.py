from django.shortcuts import render, redirect
from usuario.models import Usuario
from .models import Regra
from usuario.models import Atividade
from aluno.models import Caracteristica
from utils.tipos import tipoCaracteristica
from django.db.models import Q      # Para fazer WHERE x=a and x=b
from django.contrib import messages


# Create your views here.
# Tela de Regras
def regras(request):
    if not request.user.is_authenticated:
        return redirect("/usuario/login")
    usuario_logado = Usuario.objects.get(user=request.user)
    atividades = Atividade.objects.all()
    restricoes = Caracteristica.objects.filter(tipo=tipoCaracteristica.FISIOLOGICA)
    beneficios = Caracteristica.objects.filter(Q(tipo=tipoCaracteristica.FISIOLOGICA) | Q(tipo=tipoCaracteristica.PREFERENCIA))
    maleficios = Caracteristica.objects.filter(Q(tipo=tipoCaracteristica.FISIOLOGICA) | Q(tipo=tipoCaracteristica.PREFERENCIA))

    if request.method == 'POST':  # if the form has been filled
        atividade = request.POST['sel_cad_atividade']
        restricao = request.POST['sel_cad_restricao']
        beneficio = request.POST['sel_cad_beneficio']
        maleficio = request.POST['sel_cad_maleficio']
        pontuacao = request.POST['in_cad_pontuacao']

        # Pega os objetos referentes a cada campo
        atividade = Atividade.objects.get(nome=atividade)
        if (restricao == ""):
            restricao = None
        else:
            restricao = Caracteristica.objects.get(descricao=restricao)
        if (beneficio == ""):
            beneficio = None
        else:
            beneficio = Caracteristica.objects.get(descricao=beneficio)
        if (maleficio == ""):
            maleficio = None

        else:
            maleficio = Caracteristica.objects.get(descricao=maleficio)

        existe = list(Regra.objects.filter(Q(atividade=atividade) &
                                      Q(restricao=restricao) &
                                      Q(beneficio=beneficio) &
                                      Q(maleficio=maleficio)))
        if (existe):
            messages.warning(request, 'Regra já existe.')
        else:
            # Cria um obj
            regra_obj = Regra(atividade=atividade,
                              restricao=restricao,
                              beneficio=beneficio,
                              maleficio=maleficio,
                              pontuacao=pontuacao,
                              dono=Usuario.objects.get(user=usuario_logado.user))
            # Salva o obj no banco de dados
            regra_obj.save()
            messages.success(request, 'Regra salva com sucesso.')


 #       regra = Regra.objects.get()
#        regra.atividade = request.POST['atividade']

#        regra.save()*/
    minhas_regras = Regra.objects.filter(dono=usuario_logado)
    outras_regras = Regra.objects.exclude(dono=usuario_logado)
    return render(request, 'regras.html', {'atividades': atividades,
                                           'restricoes': restricoes,
                                           'beneficios': beneficios,
                                           'maleficios': maleficios,
                                           'minhas_regras': minhas_regras,
                                           'outras_regras': outras_regras})

