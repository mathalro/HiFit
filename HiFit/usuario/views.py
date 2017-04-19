from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from utils.tipos import TIPO
from django.core.mail import send_mail
from usuario.forms import FaleConoscoForm

MIN_SIZE_PASS = 5


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
		#Verificar formato
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
		print(user_type + " user tipo " + str(TIPO['INSTRUTOR']))
		if user_type == str(TIPO['INSTRUTOR']):
			messages.warning(request, "Pagina das bixas  (Higuete e Caminha). ")
			return render(request, 'login.html', {'user': username})
		else:
			messages.warning(request, "Pagina das outras bixas  (Renanzin e Pedrao). ")
			return render(request, 'login.html', {'user': username})
	return render(request, 'cadastro.html',{})

def fale_conosco(request):
	if request.method == 'POST':
		form = FaleConoscoForm(request.POST)
		if form.is_valid():
			send_mail(form.cleaned_data['tipo'] + ' - ' + form.cleaned_data['assunto'], form.cleaned_data['conteudo'],
			'hifites@gmail.com', ['hifites@gmail.com'])
			return redirect('/')
	else:
		form = FaleConoscoForm()

	return render(request, 'fale_conosco.html', {'form': form})
