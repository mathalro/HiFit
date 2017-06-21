from django import forms
import datetime
from usuario.models import Usuario


TIPO_CHOICES = (
    ('Suporte', 'Suporte'),
    ('Feedback', 'Feedback do sistema')
)

TIPO_POST = (
    (0, 'Público'),
    (1, 'Privado'),
)

DATE_INPUT_FORMATS = ('%d-%m-%Y')

TIPO_USUARIO = (
    ('Aluno', 1),
    ('Instrutor', 2)
)

today = datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d').strftime('%d/%m/%Y')

class PostagemForm(forms.Form):
    post = forms.CharField(label="", widget=forms.Textarea(attrs={'class' : 'form-control', 'style': 'width: 98.5%; margin-bottom: 10px; resize: none;', 'placeholder': "Escreva uma postagem...", 'rows': 3}))    
    tipo = forms.ChoiceField(required=True, label="", choices=TIPO_POST, widget=forms.Select(attrs={'class' : 'form-control', 'style': 'width: 90px'}))


class FaleConoscoForm(forms.Form):
    tipo = forms.ChoiceField(required=True, choices = TIPO_CHOICES)
    assunto = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    conteudo = forms.CharField(required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control'}))


class CadastroForm(forms.Form):
    data = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"DD/MM/AAAA"}))
    phone = forms.RegexField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"(99)99999-9999"}), regex=r'^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', 
                                error_message = ("Telefone deve estar no formado (99)99999-9999."))
    def clean_data(self):
        data = self.cleaned_data['data']
        if data > datetime.date.today() or data < datetime.date(1900, 1, 1):
            raise forms.ValidationError("Data deve estar no formado DD/MM/AAAA e ao menos ano 1900")
        return data

class EditarForm(forms.Form):
    data = forms.DateField(required=False, label="Modificar data: ",widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.RegexField(required=False, label="Modificar telefone: ",widget=forms.TextInput(attrs={'class':'form-control'}), regex=r'^\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', 
                                error_message = ("Telefone deve estar no formado (99)99999-9999."))
    def clean_data(self):
        data = self.cleaned_data['data']
        if data == None or data > datetime.date.today() or data < datetime.date(1900, 1, 1):
            raise forms.ValidationError("The date cannot be in the future!")
        return data

class EstatisticasForm(forms.Form):
    inicial = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': today}))
    final = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': today}))
    
    def clean_inicial(self):
        inicial = self.cleaned_data['inicial']
        if inicial < datetime.date(2017, 1, 1):
            raise forms.ValidationError("O periodo inicial minimo 01/01/2017!")
        elif inicial > datetime.date.today():
            raise forms.ValidationError("O periodo inicial não pode estar no futuro!")
        return inicial

    def clean_final(self):
        final = self.cleaned_data['final']
        if final > datetime.date.today():
            raise forms.ValidationError("O periodo inicial não pode estar no futuro!")
        return final