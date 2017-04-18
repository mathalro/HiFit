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
	dadosTecnicos = forms.CharField(label="Descreva-se abaixo para melhorar seu perfil",
		widget=forms.Textarea(attrs={'class' : 'form-control'}))	

