from django.shortcuts import render, redirect
from usuario.models import Usuario
from .models import Regra
from usuario.models import Atividade
from aluno.models import Caracteristica
from utils.tipos import tipoCaracteristica
from django.db.models import Q      # Para fazer WHERE x=a and x=b
from django.contrib import messages

msg_regra_salva = 'Regra salva com sucesso.'
msg_regra_existente = 'Regra já existe.'
msg_regra_nao_existente = 'Regra não existe.'
msg_regra_atualizada = 'Regra atualizada com sucesso.'
msg_regra_excluida = 'Regra excluída com sucesso.'
msg_regra_nao_alterada = 'Não houve alterações na regra.'


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
    if request.method == 'POST':
        # ----- Salvar regra
        if "salvarRegra" in request.POST:
            # Le os campos
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

            # Verifica se a regra ja existe
            if (existeRegra(atividade, restricao, beneficio, maleficio)):
                messages.warning(request, msg_regra_existente)
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
                messages.success(request, msg_regra_salva)

        # ---------- Atualizar regra
        elif "atualizarRegra" in request.POST:
            # Le os campos
            atividade = request.POST['sel_edit_atividade']
            restricao = request.POST['sel_edit_restricao']
            beneficio = request.POST['sel_edit_beneficio']
            maleficio = request.POST['sel_edit_maleficio']
            pontuacao = request.POST['in_edit_pontuacao']
            id_regra  = request.POST['in_edit_id']

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
                messages.warning(request, msg_regra_existente)
            else:
                regra_anterior = Regra.objects.get(id=id_regra)
                if (atividade == regra_anterior.atividade and restricao==regra_anterior.restricao and
                             beneficio==regra_anterior.beneficio and maleficio==regra_anterior.maleficio):
                    messages.warning(request, msg_regra_nao_alterada)
                else:
                    regra_anterior.atividade=atividade
                    regra_anterior.restricao=restricao
                    regra_anterior.beneficio=beneficio
                    regra_anterior.maleficio=maleficio
                    regra_anterior.pontuacao=pontuacao
                    regra_anterior.save(update_fields=['atividade', 'restricao', 'beneficio', 'maleficio', 'pontuacao'])
                    messages.success(request, msg_regra_atualizada)

    if (request.method == "GET"):
        if "excluirRegra" in request.GET:
            id_regra = request.GET['regra_del_id']
            regra = Regra.objects.get(id=id_regra)
            if (regra):
                regra.delete()
                messages.success(request, msg_regra_excluida)
            else:
                messages.warning(request, msg_regra_nao_existente)

    # Salva regras do usuário e de outros usuários no context
    minhas_regras = Regra.objects.filter(dono=usuario_logado)
    outras_regras = Regra.objects.exclude(dono=usuario_logado)
    return render(request, 'regras.html', {'atividades': atividades,
                                           'restricoes': restricoes,
                                           'beneficios': beneficios,
                                           'maleficios': maleficios,
                                           'minhas_regras': minhas_regras,
                                           'outras_regras': outras_regras})


# -----------------------------------------------
# Retorna se a regra ja esta cadastrada no banco
def existeRegra(atividade, restricao, beneficio, maleficio):
    existe = list(Regra.objects.filter(Q(atividade=atividade) &
                                       Q(restricao=restricao) &
                                       Q(beneficio=beneficio) &
                                       Q(maleficio=maleficio)))
    return existe