from django import forms

TIPO_CHOICES = (
    ('Suporte', 'Suporte'),
    ('Feedback', 'Feedback do sistema')
)

class FaleConoscoForm(forms.Form):
    tipo = forms.ChoiceField(required=True, choices = TIPO_CHOICES)
    assunto = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    conteudo = forms.CharField(required=True, max_length=500, widget=forms.Textarea(attrs={'class':'form-control'}))
