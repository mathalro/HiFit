from django.shortcuts import render,redirect
from .forms import *
from utils.tipos import TIPO

# Create your views here.
def cadastroInstrutor(request):
	if request.method == 'POST':
		cadastroDadosTecnicos = FormularioDadosTecnicos(request.POST)
		if cadastroDadosTecnicos.is_valid():
			usernameLogado = request.user.username
			user = User.objects.get(username=usernameLogado)
			instrutorLogado = Usuario.objects.get(user=user)
			instrutorLogado.profissao = cadastroDadosTecnicos.cleaned_data.get('profissao')
			instrutorLogado.descricao = cadastroDadosTecnicos.cleaned_data.get('dadosTecnicos')
			instrutorLogado.save()
			return redirect("/instrutor/cadastro")
		else:
			return redirect("/instrutor/cadastro")
	else:
		cadastroDadosTecnicos = FormularioDadosTecnicos()
	
	context = {
		'titulo' 		 	: 'Cadastro - Instrutor',
		'cadastroDadosTecnicos' : cadastroDadosTecnicos,
	}
	
	return render(request,'gerenciamento_instrutor.html',context)
