from datetime import datetime

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
        dt_inicial_obj = datetime.strptime(dt_inicial, '%d%m%Y').date()
        dt_final_obj = datetime.strptime(dt_final, '%d%m%Y').date()
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