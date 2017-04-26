from django import forms
import datetime
from usuario.models import Usuario


TIPO_CHOICES = (
    ('Suporte', 'Suporte'),
    ('Feedback', 'Feedback do sistema')
)

DATE_INPUT_FORMATS = ('%d-%m-%Y')

TIPO_USUARIO = (
    ('Aluno', 1),
    ('Instrutor', 2)
)

class FaleConoscoForm(forms.Form):
    tipo = forms.ChoiceField(required=True, choices = TIPO_CHOICES)
    assunto = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    conteudo = forms.CharField(required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control'}))


class CadastroForm(forms.Form):
    data = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.RegexField(widget=forms.TextInput(attrs={'class':'form-control'}), regex=r'^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', 
                                error_message = ("O telefone deve estar no formato: '(99)99999-9999'. "))
    def clean_data(self):
        data = self.cleaned_data['data']
        if data > datetime.date.today() or data < datetime.date(1900, 1, 1):
            raise forms.ValidationError("The date cannot be in the future!")
        return data

class EditarForm(forms.Form):
    data = forms.DateField(required=False, label="Modificar data: ",widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.RegexField(required=False, label="Modificar telefone: ",widget=forms.TextInput(attrs={'class':'form-control'}), regex=r'^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', 
                                error_message = ("O telefone deve estar no formato: '(99)99999-9999'. "))
    def clean_data(self):
        data = self.cleaned_data['data']
        if data == None or data > datetime.date.today() or data < datetime.date(1900, 1, 1):
            raise forms.ValidationError("The date cannot be in the future!")
        return data