from django import forms
from usuario.models import Atividade
from aluno.models import Caracteristica
from utils.tipos import tipoCaracteristica
from django.db.models import Q      # Para fazer WHERE x=a and x=b


class regrasCadastroForm(forms.Form):
    # Peganndo os valores dos campos do banco de dados
    atividades = Atividade.objects.all()
    restricoes = Caracteristica.objects.filter(tipo=tipoCaracteristica.FISIOLOGICA).values_list('descricao', flat=True)
    beneficios = Caracteristica.objects.filter(Q(tipo=tipoCaracteristica.FISIOLOGICA) | Q(tipo=tipoCaracteristica.PREFERENCIA)).values_list('descricao', flat=True)
    maleficios = Caracteristica.objects.filter(Q(tipo=tipoCaracteristica.FISIOLOGICA) | Q(tipo=tipoCaracteristica.PREFERENCIA)).values_list('descricao', flat=True)

    # Setando os valores dos campos
    atividade = forms.ModelChoiceField(queryset=atividades,
                                       empty_label="Selecione uma opção",
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    restricao = forms.ModelChoiceField(queryset=restricoes,
                                       empty_label='Selecione uma opção',
                                       widget=forms.Select(attrs={'class': 'form-control'}),
                                       label='Restrição:')
    beneficio = forms.ModelChoiceField(queryset=beneficios,
                                       empty_label='Selecione uma opção',
                                       widget=forms.Select(attrs={'class': 'form-control'}),
                                       label='Benefícios:')
    maleficio = forms.ModelChoiceField(queryset=maleficios,
                                       empty_label='Selecione uma opção',
                                       widget=forms.Select(attrs={'class': 'form-control'}),
                                       label='Malefícios:')

    pontuacao = forms.CharField(max_length=2,
                                widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                label='Pontuação:')


#class regrasEdicaoForm(forms.Form):
