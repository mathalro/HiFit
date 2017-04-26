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

MIN_SIZE_PASS = 5

import re

def home(request):
	return render(request, 'base.html',{})


def login(request):
	if request.user.is_authenticated:
		return redirect("/")
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			auth_login(request, user)
			return redirect("/")
		else:
			messages.warning(request, "Usuário e/ou senha incorretos. ")
			return redirect('/usuario/login')

	return render(request, 'login.html',{})


def logout(request):
	auth_logout(request)
	return redirect('/usuario/login')


def cadastro(request):
	if request.user.is_authenticated:
		return redirect("/")

	if request.method == 'POST':
		user_type = request.POST['user_type']
		name = request.POST['name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		phone = request.POST['phone']
		date = request.POST['date']
		#Verificar formato e entre 1900 e dia atual
		allright = True

		#Testa existencia de usuario com mesmo username
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None
		if user is not None:
			messages.warning(request, "Usuário já cadastrado. ")
			allright = Falses

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
		
		user = User.objects.create_user(username, email, password)
		new_user = Usuario(user=user, tipo_usuario=int(user_type), datanascimento=date, telefone=phone, nome=name)
		new_user.save()
		messages.success(request, "Cadastro realizado com sucesso. Logue no sistema.")
		
		return redirect('/usuario/login')

	return render(request, 'cadastro.html',{})

def gerenciar(request):

	current_user = Usuario.objects.get(user=request.user)
	name = current_user.nome
	username = current_user.user.username
	phone = current_user.telefone
	date = current_user.datanascimento

	print(request.POST)

	if 'excluir' in request.POST:
		auth_logout(request)
		user = User.objects.get(username=username)
		user.delete()
		current_user.delete()
		return redirect('/usuario/login')	

	if request.method == 'POST':
		name = name if request.POST['name'] is None else request.POST['name'] 
		new_username = username if request.POST['username'] is None == "" else request.POST['username']
		phone = phone if request.POST['phone'] is None else request.POST['phone']
		date = date if request.POST['date'] is None else request.POST['date']
		allright = True

		if new_username != username:
			try: #Testa existencia de usuario com mesmo username
				user = User.objects.get(username=new_username)
			except User.DoesNotExist:
				user = None
			
			if user is not None:
				messages.warning(request, "Nome de usuário já existe. ")
				allright = False
		
		current_user.user.username = new_username
		current_user.user.save()
		current_user.nome = name
		current_user.telefone = phone
		current_user.datanascimento = date
		current_user.save(update_fields=['nome', 'user', 'telefone', 'datanascimento'])
		messages.success(request, "Edição realizado com sucesso. Logue no sistema.")
		
		return redirect('/usuario/gerenciar')

	return render(request, 'gerenciar.html',{'user': current_user})


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
