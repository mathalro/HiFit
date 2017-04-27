from enum import IntEnum

TIPO = {
	'ALUNO' : 1,
	'INSTRUTOR' : 2
}

class tipoCaracteristica(IntEnum):
    PREFERENCIA = 0
    ALTURA = 1
    PESO = 2
    DOENCA = 3
    DIFICULDADE_MOTORA = 4
    BENEFICIO = 5
    MALEFICIO = 6


PALAVRAS_BAIXO_CALAO = [
    'caralho',
    'merda'
]

TIPOS_IDENTIFICACAO = (
    ('CRM', 'CRM'),
    ('CREFITO', 'CREFITO'),
    ('CREF', 'CREF'),
)