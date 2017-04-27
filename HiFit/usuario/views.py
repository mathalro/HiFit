from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Usuario, Classificacao
from utils.tipos import TIPO, PALAVRAS_BAIXO_CALAO
from django.core.mail import send_mail
from usuario.forms import FaleConoscoForm
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario
from .forms import CadastroForm, EditarForm
import uuid

MIN_SIZE_PASS = 5

import re

def home(request):
	if request.user.is_authenticated:
		usuario = Usuario.objects.get(user=request.user)
		context = {
			'aluno' : usuario.isAluno()
		}
		return render(request, 'base.html',context)
	return render(request, 'base.html',{'aluno': False})


def login(request):
	if request.user.is_authenticated:
		return redirect("/")
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			usuario = Usuario.objects.get(user = user)
			if usuario.situacao == 0:
				messages.warning(request, "Usuario ainda não foi ativado, acesse seu email e clique no link de ativação.")
				return redirect("/usuario/login")
			else:
				auth_login(request, user)
				return redirect("/")
		else:
			messages.warning(request, "Usuário e/ou senha incorretos. ")
			return redirect('/usuario/login')

	return render(request, 'login.html',{})


def confirmar(request):
	if request.user.is_authenticated:
		return redirect("/")

	try:
		usuario = Usuario.objects.get(auth_id=request.GET['auth'])
	except:
		usuario = None
		messages.warning(request, "Codigo de autenticação inválido. ")	

	if usuario is not None:
		if usuario.situacao == 0:
			usuario.situacao = 1
			usuario.save()
			messages.warning(request, "Usuario ativado com sucesso. ")
		else:
			messages.warning(request, "Usuario já está ativo. ")
	
	return redirect('/usuario/login')


@login_required(login_url="/usuario/login/")
def logout(request):
    auth_logout(request)
    return redirect('/usuario/login')


def recuperar(request):
	if request.user.is_authenticated:
		return redirect("/")

	if request.method == 'POST':
		try:
			user = User.objects.get(email = request.POST['email'])
		except:
			user = None
			messages.warning(request, "Email não cadastrado. ")
			return redirect('/usuario/recuperar')

		if user is not None:
			usuario = Usuario.objects.get(user=user)
			auth_id = uuid.uuid4().hex
			usuario.auth_id = auth_id
			usuario.situacao = 2
			usuario.save()
			send_mail('Recuperação de senha', \
						"Solicitação de alteração de senha.\n\
						Usuário: " + user.username + "\n\
						Link de recuperação: http://localhost:8000/usuario/valida-token-senha?auth=" + auth_id + "\n\n\
						Atenciosamente,\n\
						Equipe HIFIT.\n\n\
						Email automatico, não responda.", \
						'hifites@gmail.com', [user.email])
			messages.warning(request, "Email de recuperação enviado. ")

			return redirect('/usuario/recuperar')

	return render(request, 'recuperar.html', {})


def alterar_senha(request):
	if request.method == 'POST':
		user = User.objects.get(username=request.POST['username'])
		password = request.POST['password']
		if len(password) < MIN_SIZE_PASS:
			messages.warning(request, "Senha muito pequena. ")
			return render(request, 'alterar-senha.html', {'username': user.username})

		user.set_password(password)
		user.save()
		usuario = Usuario.objects.get(user = user)
		usuario.situacao = 1
		usuario.save()
		user = authenticate(username=user.username, password=password)
		auth_login(request, user)
		messages.warning(request, "Senha alterada com sucesso. ")
		return redirect('/usuario/login/')

	return render(request, 'alterar-senha.html', {})


def valida_token_senha(request):
	if request.user.is_authenticated:
		return redirect("/")

	try:
		usuario = Usuario.objects.get(auth_id=request.GET['auth'])
	except:
		usuario = None
		messages.warning(request, "Codigo de recuperação inválido. ")	
		return redirect ('/usuario/recuperar')

	if usuario is not None:
		if usuario.situacao != 2:
			messages.warning(request, "Link de recuperação já foi utilizado. ")
			return redirect ('/usuario/recuperar')
		else:		
			return render(request, 'alterar-senha.html', {'username': usuario.user.username})


def cadastro(request):
	if request.user.is_authenticated:
		return redirect("/")

	if request.method == 'POST':
		cadastroDados = CadastroForm(request.POST)
		if cadastroDados.is_valid():
			user_type = request.POST['user_type']
			name = request.POST['name']
			email = request.POST['email']
			username = request.POST['username']
			password = request.POST['password']
			phone = cadastroDados.cleaned_data.get('phone')
			data = cadastroDados.cleaned_data.get('data')
			
			print(cadastroDados.cleaned_data)
			#Verificar formato e entre 1900 e dia atual
			allright = True

			#Testa existencia de usuario com mesmo username
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				user = None
			if user is not None:
				messages.warning(request, "Usuário já cadastrado. ")
				allright = False

			#Testa existencia de usuario com mesmo email
			try:
				user = User.objects.get(email=email)
			except User.DoesNotExist:
				user = None
			if user is not None:
				messages.warning(request, "Email já cadastrado. ")
				allright = False
			
			#Testa se a senha possui tamanho minimo
			if len(password) < MIN_SIZE_PASS:
				messages.warning(request, "Senha muito pequena. ")
				allright = False	
			if not allright:
				return redirect('/usuario/cadastro')
			
			auth_id = uuid.uuid4().hex

			user = User.objects.create_user(username, email, password)
			new_user = Usuario(user=user, tipo_usuario=int(user_type), datanascimento=data, telefone=phone, nome=name, auth_id=auth_id, situacao=0)
			new_user.save()
			send_mail('Confirmacao', \
						"Parabéns! Seu cadastro foi realizado com sucesso!\n\
						Usuário: " + username + "\n\
						Link de ativação: http://localhost:8000/usuario/confirmar?auth=" + auth_id + "\n\n\
						Atenciosamente,\n\
						Equipe HIFIT.\n\n\
						Email automatico, não responda.", \
						'hifites@gmail.com', [email])
			messages.success(request, "Cadastro realizado com sucesso. Acesse seu email para confirmação.")
			
			return redirect('/usuario/login')

		else:
			if cadastroDados.has_error('phone'):
				messages.warning(request, "Telefone deve estar no formado (99)99999-9999")
			if cadastroDados.has_error('data'):
				messages.warning(request, "Data deve estar no formado DD/MM/AAAA e ao menos ano 1900")
			return redirect('/usuario/cadastro')

	cadastroDados = CadastroForm()
	return render(request, 'cadastro.html',{'cadastroDados': cadastroDados} )

@login_required(login_url="/usuario/login/")
def gerenciar(request):
	current_user = Usuario.objects.get(user=request.user)
	name = current_user.nome
	phone = current_user.telefone
	data = current_user.datanascimento

	if 'excluir' in request.POST:
		auth_logout(request)
		user = User.objects.get(username=current_user.user.username)
		user.delete()
		current_user.delete()
		return redirect('/usuario/login')

	if 'alterar-senha' in request.POST:
		return render(request, 'alterar-senha.html', {'username': current_user.user.username})	

	if request.method == 'POST':
		user2 = authenticate(username = current_user.user.username, password = request.POST['password'])
		if user2 is not None:
			editarDados = EditarForm(request.POST)
			if editarDados.has_error('phone'):
				phone = current_user.telefone
				messages.warning(request, "Telefone deve estar no formado (99)99999-9999")
			else:
				phone = editarDados.cleaned_data.get('phone')
			if editarDados.has_error('data'):
				data = current_user.datanascimento
				messages.warning(request, "Data deve estar no formado DD/MM/AAAA e ao menos ano 1900")
			else:
				data = editarDados.cleaned_data.get('data')				
			name = name if request.POST['name'] is None else request.POST['name'] 
			current_user.nome = name
			current_user.telefone = phone
			current_user.datanascimento = data
			current_user.save(update_fields=['nome', 'telefone', 'datanascimento'])
			messages.success(request, "Edição realizado com sucesso. Logue no sistema.")
		else:
			messages.warning(request, "Senha inválida.")
		return redirect('/usuario/gerenciar')
	

	editarDados = EditarForm()

	aluno = current_user.isAluno()
	return render(request, 'gerenciar.html',{'user': current_user, 'editarDados': editarDados, 'aluno': aluno})


@login_required(login_url="/usuario/login/")
def fale_conosco(request):
    if request.method == 'POST':
        form = FaleConoscoForm(request.POST)
        if form.is_valid():
            # Verifica existencia de palavras de baixo calao no texo
            for palavra in PALAVRAS_BAIXO_CALAO:
                if re.search(palavra, form.cleaned_data['assunto'].lower()) or re.search(palavra, form.cleaned_data['conteudo'].lower()):
                    messages.warning(request, 'Não se pode enviar mensagem contendo palavra(s) de baixo calão.')
                    return redirect('/fale-conosco')
            send_mail(form.cleaned_data['tipo'] + ' - ' + form.cleaned_data['assunto'], form.cleaned_data['conteudo'],
            'hifites@gmail.com', ['hifites@gmail.com'])
            messages.success(request, "Sua mensagem foi enviada com sucesso.")

            return redirect('/fale-conosco')
    else:
        form = FaleConoscoForm()

    # Pega informacoes do usuario logado
    username = request.user.username
    usuario = User.objects.get(username=username)
    usuario_logado = Usuario.objects.get(user=usuario)

    # Define a url
    if usuario_logado.tipo_usuario == TIPO['ALUNO']:
        url = 'fale_conosco_aluno.html'
    else:
        url = 'fale_conosco_instrutor.html'

    return render(request, url, {'form': form})
