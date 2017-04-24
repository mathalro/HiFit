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
    # Reaproveitando algumas partes do codigo para cadastro e edicao
    if request.method == 'POST' or request.method == 'PATCH':
        # Le os campos
        if request.method == 'POST': 
            atividade = request.POST['sel_cad_atividade']
            restricao = request.POST['sel_cad_restricao']
            beneficio = request.POST['sel_cad_beneficio']
            maleficio = request.POST['sel_cad_maleficio']
            pontuacao = request.POST['in_cad_pontuacao']
        if request.method == 'PATCH':
            atividade = request.PATCH['sel_edit_atividade']
            restricao = request.PATCH['sel_edit_restricao']
            beneficio = request.PATCH['sel_edit_beneficio']
            maleficio = request.PATCH['sel_edit_maleficio']
            pontuacao = request.PATCH['in_edit_pontuacao']
            id_regra  = request.PATCH['in_edit_id']
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

        # Verifica se a regra ja existe
        if (existeRegra(atividade, restricao, beneficio, maleficio)):
            messages.warning(request, 'Regra já existe.')
        else:
            if request.method == 'POST':
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
            elif request.method == 'PATCH':
                regra_anterior = Regra.objects.filter(id=id_regra)
                if (atividade == regra_anterior.atividade and restricao==regra_anterior.restricao and
                             beneficio==regra_anterior.beneficio and maleficio==regra_anterior.maleficio):
                    messages.warning(request, 'Não houve alterações na regra.')
                else:
                    regra_anterior.update(atividade=atividade,
                                  restricao=restricao,
                                  beneficio=beneficio,
                                  maleficio=maleficio,
                                  pontuacao=pontuacao)
                    messages.success(request, 'Regra atualizada com sucesso.')

    minhas_regras = Regra.objects.filter(dono=usuario_logado)
    outras_regras = Regra.objects.exclude(dono=usuario_logado)
    return render(request, 'regras.html', {'atividades': atividades,
                                           'restricoes': restricoes,
                                           'beneficios': beneficios,
                                           'maleficios': maleficios,
                                           'minhas_regras': minhas_regras,
                                           'outras_regras': outras_regras})


# Retorna se a regra ja esta cadastrada no banco
def existeRegra(atividade, restricao, beneficio, maleficio):
    existe = list(Regra.objects.filter(Q(atividade=atividade) &
                                       Q(restricao=restricao) &
                                       Q(beneficio=beneficio) &
                                       Q(maleficio=maleficio)))
    return existe