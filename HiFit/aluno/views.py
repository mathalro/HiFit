# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from usuario.models import Usuario
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from datetime import date

import re


@login_required(login_url="/usuario/login/")
def gerenciamento_aluno(request):

    # Iniciar variaveis
    cadastro = 'completo'

    # Pega informacoes do usuario logado
    user_logado = request.user.username
    usuario = User.objects.get(username=user_logado)
    aluno_logado = Usuario.objects.get(user=usuario)
    lista_caracteristicas = [{'descricao': c.descricao, 'valor': c.valor, 'tipo': c.tipo} for c in
                             aluno_logado.caracteristicas.all()]
    lista_descricao = [d['descricao'] for d in lista_caracteristicas]
    lista_tipo = [d['tipo'] for d in lista_caracteristicas]

    # Constroi lista de acordo com o tipo
    lista_preferencias = [l for l in lista_caracteristicas if TipoCaracteristica.PREFERENCIA.value == l['tipo']]
    lista_doenca = [l for l in lista_caracteristicas if TipoCaracteristica.DOENCA.value == l['tipo']]
    lista_dificuldade_motora = [l for l in lista_caracteristicas if
                                TipoCaracteristica.DIFICULDADE_MOTORA.value == l['tipo']]

    # Cria form e preenche com valores ja cadastrados
    form = gerenciamentoAlunoForm()
    if aluno_logado.caracteristicas.all():

        # Altura
        aluno_logado_altura = aluno_logado.caracteristicas.filter(tipo=TipoCaracteristica.ALTURA.value)
        if aluno_logado_altura:
            form.fields['altura'].initial = aluno_logado_altura[0].descricao

        # Peso
        aluno_logado_peso = aluno_logado.caracteristicas.filter(tipo=TipoCaracteristica.PESO.value)
        if aluno_logado_peso:
            form.fields['peso'].initial = aluno_logado_peso[0].descricao

    if request.method == 'POST':
         ###################################################
        #                                                   #
        # Menus: Preferencia & Caracteristicas Fisiológicas #
        #                                                   #
         ###################################################

        # Salvar
        if 'salvar' in request.POST:

            # Percorre o request.POST buscando por select_field_*
            for select in request.POST:

                if re.match('select_field', select):

                    # Checa se a caracteristica nao esta cadastrada em Caracteristica
                    # caso afirmativo entao a nova caracteristica e' cadastrada e associada com o usuario
                    if request.POST[select] not in [c.descricao for c in Caracteristica.objects.all()]:

                        # Cria a cracteristica
                        caracteristica = Caracteristica(descricao=request.POST[select])
                        caracteristica.save()
                        # Salva a caracteristica do aluno
                        aluno_logado.caracteristicas.add(caracteristica)
                        messages.success(request, 'Característica \'' + request.POST[select] + '\' cadastrada com sucesso.')

                    # Checa se o usuario nao possui a caracteristica
                    # caso nao possua apenas associa a caracteristica a ele
                    # caso contrario nao faz nada
                    elif request.POST[select] not in lista_descricao:

                        # Salva a caracteristica do aluno
                        aluno_logado.caracteristicas.add(Caracteristica.objects.get(descricao=request.POST[select]))
                        messages.success(request, 'Característica \'' + request.POST[select] + '\' cadastrada com sucesso.')

            return redirect("/aluno/gerenciar")

        # Excluir
        elif 'excluir' in request.POST:

            # Caracteristica para ser deletada
            carac_del = request.POST['excluir'].replace("_", " ")

            # Checa se o que quer ser deletado ja foi criado pelo usuario
            if carac_del in lista_descricao:

                aluno_logado.caracteristicas.remove(Caracteristica.objects.get(descricao=carac_del))
                messages.success(request, 'Característica \'' + carac_del + '\' excluída com sucesso.')

            return redirect("/aluno/gerenciar")

         ##############################
        #                              #
        # Menu: Caracteristicas Física #
        #                              #
         ##############################

        form = gerenciamentoAlunoForm(request.POST)

        # Caso o form esteja valido
        if form.is_valid():

            # Caso a caracteristica altura seja nova
            if TipoCaracteristica.ALTURA.value not in lista_tipo:

                caracteristica = Caracteristica(descricao=str(form.cleaned_data.get('altura')),
                                                valor=ValorCaracteristica.ALTURA.value,
                                                tipo=TipoCaracteristica.ALTURA.value)
                caracteristica.save()
                aluno_logado.caracteristicas.add(caracteristica)

            else:
                aluno_logado.caracteristicas.filter(tipo=TipoCaracteristica.ALTURA.value).update(descricao=str(form.cleaned_data.get('altura')))

            # Caso a caracteristica peso seja nova
            if TipoCaracteristica.PESO.value not in lista_tipo:

                caracteristica = Caracteristica(descricao=str(form.cleaned_data.get('peso')),
                                                valor=ValorCaracteristica.PESO.value,
                                                tipo=TipoCaracteristica.PESO.value)
                caracteristica.save()
                aluno_logado.caracteristicas.add(caracteristica)

            else:
                aluno_logado.caracteristicas.filter(tipo=TipoCaracteristica.PESO.value).update(descricao=str(form.cleaned_data.get('peso')))

            messages.success(request, 'Característica cadastrada com sucesso.')
            return redirect("/aluno/gerenciar")

    
    # Checa o que o usuario já cadastrou
    if not lista_preferencias and not (TipoCaracteristica['ALTURA'].value in lista_tipo) and not (TipoCaracteristica['ALTURA'].value in lista_tipo) and not lista_doenca and not lista_dificuldade_motora:
        messages.warning(request, 'Você deve cadastrar uma preferência, todas as características físicas e uma característica fisiológica \
                         para ter acesso a outras funcionalidades.')
        cadastro = 'incompleto'
    elif not lista_preferencias and not (TipoCaracteristica['ALTURA'].value in lista_tipo) and not (TipoCaracteristica['ALTURA'].value in lista_tipo):
        messages.warning(request, 'Você deve cadastrar uma preferência e todas as características físicas \
                         para ter acesso a outras funcionalidades.')
        cadastro = 'incompleto'
    elif not lista_preferencias and not lista_doenca and not lista_dificuldade_motora:
        messages.warning(request, 'Você deve cadastrar uma preferência e uma característica fisiológica \
                         para ter acesso a outras funcionalidades.')
        cadastro = 'incompleto'
    elif not (TipoCaracteristica['ALTURA'].value in lista_tipo) and not (TipoCaracteristica['ALTURA'].value in lista_tipo) and not lista_doenca and not lista_dificuldade_motora:
        messages.warning(request, 'Você deve cadastrar todas as características físicas e uma característica fisiológica \
                         para ter acesso a outras funcionalidades.')
        cadastro = 'incompleto'
    elif not lista_preferencias:
        messages.warning(request, 'Você deve cadastrar uma preferência \
                         para ter acesso a outras funcionalidades.')
        cadastro = 'incompleto'
    elif not (TipoCaracteristica['ALTURA'].value in lista_tipo) and not (TipoCaracteristica['ALTURA'].value in lista_tipo):
        messages.warning(request, 'Você deve cadastrar todas as características físicas \
                         para ter acesso a outras funcionalidades.')
        cadastro = 'incompleto'
    elif not lista_doenca and not lista_dificuldade_motora:
        messages.warning(request, 'Você deve cadastrar uma característica fisiológica \
                         para ter acesso a outras funcionalidades.')
        cadastro = 'incompleto'

    return render(request, 'gerenciamento_aluno.html', {'form': form,
                                                        'cadastro': cadastro,
                                                        'lista_preferencias': lista_preferencias,
                                                        'lista_doenca': lista_doenca,
                                                        'lista_dificuldade_motora': lista_dificuldade_motora})



@login_required(login_url="/usuario/login/")
def historico_recomendacoes(request):
    #pega uma lista de recomendacoes ordenadas de forma descendente primeiramente
    #classificação do instrutor no sistema e depois pela data.
    recomendacoes = Recomendacao.objects.filter().order_by('-instrutor__classificacao__somapessoas','-data')
    filtro_data = filtroPorDataRecomendacoes()
    if request.method == "POST":
        #requisiçao do filtro por caracteristica
        if "filtro_caracteristica" in request.POST:
            #resgatando altura e peso do aluno solicitante:
            solicitante = Usuario.objects.get(user=request.user)
            altura_solicitante = solicitante.caracteristicas.get(tipo=1).descricao
            peso_solicitante = solicitante.caracteristicas.get(tipo=2).descricao
            #resgatando todas as características tipo 1 e 2 do sistema:
            aluno_semelhante = []
            recomendacoes = []
            for aluno in Usuario.objects.filter(tipo_usuario=1):
                try:
                    altura = aluno.caracteristicas.get(tipo=1).descricao
                except Caracteristica.DoesNotExist:
                    altura = None
                try:
                    peso = aluno.caracteristicas.get(tipo=2).descricao
                except Caracteristica.DoesNotExist:
                    peso = None
                if aluno != solicitante and altura_solicitante == altura and peso_solicitante == peso:
                    aluno_semelhante.append(aluno)
                    #armazena as recomendacoes feitas aquele aluno
                    for recomendacao in Recomendacao.objects.filter(aluno=aluno):
                        recomendacoes.append(recomendacao)
            recomendacoes = sorted(recomendacoes, key=getKeyInstrutor)
            recomendacoes = sorted(recomendacoes, key=getKeyData, reverse=True)
        else:
            #requisição para filtrar por data, ainda mantém a ordenação pela classificação do instrutor.
            filtro_data = filtroPorDataRecomendacoes(request.POST)
            if filtro_data.is_valid():
                data_corte = filtro_data.cleaned_data.get("data_corte")
                recomendacoes = Recomendacao.objects.filter(data__lte=data_corte).order_by('-instrutor__classificacao__somapessoas','-data',)
            else:
                messages.warning(request,"Data inválida: data informada é futura, informe novamente.")
    else:   
        filtro_data = filtroPorDataRecomendacoes()
    context = {
        'recomendacoes': recomendacoes,
        'filtro_data'  : filtro_data
    }
       
    return render(request,"historico_recomendacoes.html",context)

#funcoes para ordenar a lista de recomendacoes quando acionado o filtro de caracteristicas
def getKeyData(recomendacao):
    return recomendacao.data
def getKeyInstrutor(recomendacao):
    return recomendacao.instrutor.classificacao.somapessoas

    