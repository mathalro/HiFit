from django.shortcuts import render,redirect
from .forms import *
from utils.tipos import TIPO
# Create your views here.
def gerenciamentoInstrutor(request):
	if request.method == 'POST':
		cadastroUser = FormularioCadastroUsuario(request.POST)
		cadastroInstrutor = FormularioCadastroInstrutor(request.POST)
		if cadastroInstrutor.is_valid() and cadastroUser.is_valid():
			instrutor = cadastroInstrutor.save(commit=False)
			user = cadastroUser.save()
			instrutor.user = user
			instrutor.tipo_usuario = TIPO['INSTRUTOR']
			instrutor.save()
			return redirect("/instrutor")
		else:
			return redirect("/instrutor")
	else:
		cadastroUser = FormularioCadastroUsuario()
		cadastroInstrutor = FormularioCadastroInstrutor()
	
	context = {
		'titulo' 		 	: 'Cadastro',
		'cadastroUser'   	: cadastroUser,
		'cadastroInstrutor' : cadastroInstrutor,
	}
	
	return render(request,'gerenciamento_instrutor.html',context)
