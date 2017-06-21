from utils.tipos import tipoCaracteristica
from datetime import datetime

class AlunoRelatorio:
    NOME            = 0
    IDADE           = 1
    ALTURA          = 2
    PESO            = 3
    RECOMENDACOES   = 4


# Mensagens
msg_relatorios_dt_formato_invalido = 'Formato da data inválido. Formato deve ser DD/MM/AA.'
msg_relatorios_dt_inicial_maior = 'Data inicial deve ser menor do que a data final.'
msg_relatorios_dt_final_maior = 'Data final deve ser maior do que a data atual.'


# Valida as datas
def validaDatas(dt_inicial, dt_final):
    mensagens = []
    dt_inicial_obj = datetime.today().date()
    dt_final_obj = datetime.today().date()
    try:
        print(dt_inicial)
        print(dt_final)
        dt_inicial_obj = datetime.strptime(dt_inicial, '%Y-%m-%d').date()
        print("passei1")
        dt_final_obj = datetime.strptime(dt_final, '%Y-%m-%d').date()
        print("passei2")
        if dt_inicial_obj >= dt_final_obj:
            mensagens.append(msg_relatorios_dt_inicial_maior)
        if dt_final_obj > datetime.today().date():
            mensagens.append(msg_relatorios_dt_final_maior)
    except ValueError:
        mensagens.append(msg_relatorios_dt_formato_invalido)
    return mensagens, dt_inicial_obj, dt_final_obj


# Retorna true se a atividade ja estiver no array
def atividadeRepetida(array, atividade):
    for a in array:
        if a == atividade:
            return True
    return False


# Calcula a media de classificacoes e retorna as atividades recomendadas
# @return float media, string atividades
def getComponentesRecomendacao(recomendacoes):
    total = 0
    atividades = []
    str_atividades = ''
    if len(recomendacoes) == 0:     # Nao ha recomendacaoes
        return "Não há recomendações.", "Não há recomendações."
    for recomendacao in recomendacoes:
        atividade = recomendacao.atividade.nome
        if not atividadeRepetida(atividades, atividade):
            atividades.append(atividade)
            str_atividades += atividade + ', '
        total += recomendacao.classificacao.somanota
    return (total / len(recomendacoes)), str_atividades[:-2]            # :-2 remove as virgulas


# Retorna true se o aluno ja estiver no array
def alunoRepetido(array, aluno):
    for i in range(0, len(array)):
        if array[i] == aluno:
            return True, i
    return False, -1


# Coloca os dados de um aluno em um vetor
def getAluno(aluno):
    caracteristicas = aluno.caracteristicas
    nome = aluno.nome
    idade = 'Não informado.'
    altura = 'Não informado.'
    peso = 'Não informado.'
    for c in caracteristicas.all():
        aux = c.tipo
        if c.tipo == tipoCaracteristica.IDADE:
            idade = c.valor
        elif c.tipo == tipoCaracteristica.ALTURA:
            altura = c.valor
        elif c.tipo == tipoCaracteristica.PESO:
            peso = c.valor
    return [nome, idade, altura, peso, []]


# Passa o array para string
def toStringAlunos(alunos):
    string= ""
    for aluno in alunos:
        string+= '<h3>' + aluno[AlunoRelatorio.NOME] + '</h3>'
        string+= '<p><b>Idade:</b> ' + str(aluno[AlunoRelatorio.IDADE]) + '</p>'
        string+= '<p><b>Altura:</b> ' + str(aluno[AlunoRelatorio.ALTURA]) + '</p>'
        string+= '<p><b>Peso:</b> ' + str(aluno[AlunoRelatorio.PESO]) + '</p>'
        string+= "<p><b>Recomendacões:</b> "
        atividades = []
        for recomendacao in aluno[AlunoRelatorio.RECOMENDACOES]:
            atividade = recomendacao.atividade
            if not atividadeRepetida(atividades, atividade):
                atividades.append(atividade.nome)
                string+= atividade.nome + ' (' + recomendacao.data.strftime("%d/%m/%Y") + ') , '
        string = string[:-2] + '</p>'
        string+= '<hr>'
    return string


# O relatório deve conter os dados do aluno: nome, idade, altura, peso, data que aceitou a recomendação.
def getDadosAlunos(recomendacoes):
    alunos = []
    for recomendacao in recomendacoes:
        aluno = getAluno(recomendacao.aluno)
        # Adiciona recomendacao aqui para o retorno da funcao ser menor
        aluno[AlunoRelatorio.RECOMENDACOES].append(recomendacao)
        # Verifica se o aluno ja possui recomendacao
        repetido, indice = alunoRepetido(alunos, aluno)
        if repetido:
            # Se sim adiciona a recomendacao para o aluno
            alunos[indice][AlunoRelatorio.RECOMENDACOES].append(recomendacao)
        else:
            alunos.append(aluno)
    return toStringAlunos(alunos)
