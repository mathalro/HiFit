from django.shortcuts import render, redirect
from django.core.mail import send_mail

from usuario.forms import FaleConoscoForm

# Create your views here.
def home(request):
	return render(request, 'index.html', {})

def fale_conosco(request):
	if request.method == 'POST':
		form = FaleConoscoForm(request.POST)
		if form.is_valid():
			send_mail(form.cleaned_data['tipo'] + ' - ' + form.cleaned_data['assunto'], form.cleaned_data['conteudo'],
			'hifites@gmail.com', ['hifites@gmail.com'])
			return redirect('/')
	else:
		form = FaleConoscoForm()

	return render(request, 'fale_conosco.html', {'form': form})
