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
		fields = ['profissao','tipo_identificacao','identificacao','descricao']
		widgets = {
			'profissao'				: forms.Select(attrs={'class' : 'form-control'}),
			'tipo_identificacao'	: forms.Select(attrs={'class' : 'form-control'}),
			'identificacao'			: forms.TextInput(attrs={'class' : 'form-control'}),
			'descricao'				: forms.Textarea(attrs={'class' : 'form-control'})
		}	
		labels = {
			'profissao' 		: 'Profissão',
			'tipo_identificacao': 'Selecione qual identificação será informada',
			'identificacao' 	: 'Digite sua identificação',
			'descricao' 		: 'Descreva-se abaixo para melhorar seu perfil'
		}

	#sobrescrevendo a funcao de validacao
	def clean(self):
		#pegando os dados validados do formulario original
		cleaned_data = super(FormularioEdicaoDadosTecnicos, self).clean()
		if cleaned_data.get("tipo_identificacao") == 'CRM':
			if len(cleaned_data.get("identificacao")) != 5:
				raise forms.ValidationError("CRM deve conter 5 digitos!")
		elif cleaned_data.get("tipo_identificacao") == 'CREFITO':
			if len(cleaned_data.get("identificacao")) != 8:
				raise forms.ValidationError("CREFITO deve conter 8 caracteres!")
		elif cleaned_data.get("tipo_identificacao") == 'CREF':
			if len(cleaned_data.get("identificacao")) != 8:
				raise forms.ValidationError("CREF deve conter 8 caracteres!")

		return cleaned_data