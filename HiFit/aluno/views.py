from django.shortcuts import render

from aluno.forms import *

# Create your views here.
def gerenciamento_aluno(request):
	if request.method == 'POST':
		form = gerenciamentoAlunoForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = gerenciamentoAlunoForm()

	return render(request, 'gerenciamento_aluno.html', {'form': form})