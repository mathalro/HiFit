from django import forms
from django.db import models
from django.forms import ModelForm
from .models import *
from usuario.models import Usuario
from django.contrib.auth.models import User
from instrutor.models import Profissao


class FormularioDadosTecnicos(forms.Form):
	profissao = forms.ModelChoiceField(label="Profissão",queryset=Profissao.objects.all(), 
		widget=forms.Select(attrs={'class' : 'form-control'}))
	identificacao = forms.CharField(label="Digite sua identificação (CRM, CREF ou CREFITO)",
		widget=forms.TextInput(attrs={'class' : 'form-control'}))
	dadosTecnicos = forms.CharField(label="Descreva-se abaixo para melhorar seu perfil",
		widget=forms.Textarea(attrs={'class' : 'form-control'}))	

class FormularioEdicaoDadosTecnicos(ModelForm):
	class Meta:
		model = Usuario
		fields = ['profissao','identificacao','descricao']
		widgets = {
			'profissao'			: forms.Select(attrs={'class' : 'form-control'}),
			'identificacao'		: forms.TextInput(attrs={'class' : 'form-control'}),
			'descricao'			: forms.Textarea(attrs={'class' : 'form-control'})
		}	
		labels = {
			'profissao' 	: 'Profissão',
			'identificacao' : 'Digite sua identificação (CRM, CREF ou CREFITO)',
			'descricao' 	: 'Descreva-se abaixo para melhorar seu perfil'
		}
