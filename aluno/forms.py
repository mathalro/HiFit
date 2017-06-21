from django import forms
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from HiFit import settings

class gerenciamentoAlunoForm(forms.Form):
    altura = forms.FloatField(label="Altura (m)",
                              min_value=0,
                              max_value=3,
                              error_messages={'invalid': 'your custom error message'},
                              widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'altura', 'step': '0.01'}))

    peso = forms.FloatField(label="Peso (Kg)",
                            min_value=0,
                            max_value=500,
                            widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'peso', 'step': '0.001'}))

class filtroPorDataRecomendacoes(forms.Form):
	data_corte = forms.DateField(label="Período antes de:",
								 widget=forms.DateInput(attrs={'class':'form-control','type' : 'date','style' : 'width:150px;'}))

	def clean_data_corte(self):
		data_corte = self.cleaned_data.get("data_corte")
		if data_corte > date.today():
			raise forms.ValidationError("Data inválida: data informada é futura, informe novamente.")

		return data_corte