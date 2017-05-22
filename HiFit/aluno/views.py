# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from usuario.models import Usuario
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    filtro_data = fitroPorDataRecomendacoes()
    if request.method == "POST":
        pass
    else:
        #pega uma lista de recomendacoes ordenadas de forma descendente por data
        recomendacoes = Recomendacao.objects.filter().order_by('-data')
        context = {
            'recomendacoes': recomendacoes,
            'filtro_data'  : filtro_data
        }
        return render(request,"historico_recomendacoes.html",context)




    