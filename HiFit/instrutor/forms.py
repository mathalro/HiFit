from django import forms
from django.db import models
from django.forms import ModelForm
from .models import *
from usuario.models import Usuario
from django.contrib.auth.models import User

class FormularioCadastroUsuario(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email']
		widgets = {
			'username' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Usuário'}),
			'password' : forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : 'Senha'}),
			'email' : forms.EmailInput(attrs={'class' : 'form-control','placeholder' : 'E-mail'}),
		}

class FormularioCadastroInstrutor(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ['nome','datanascimento','telefone','cpf','identificacao','profissao']
		widgets = {
			'nome' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nome'}),
			'datanascimento' : forms.DateInput(attrs={'class' : 'form-control','placeholder' : 'Data de Nascimento - DD/MM/AAAA'}),
			'telefone' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Telefone'}),
			'cpf' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'CPF'}),
			'identificacao' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Identificação'}),
			'profissao' : forms.Select(attrs={'class' : 'form-control','placeholder' : 'Profissão'})
		}