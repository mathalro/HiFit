import enum

from enum import IntEnum

TIPO = {
    'ALUNO' : 1,
    'INSTRUTOR' : 2
}

PALAVRAS_BAIXO_CALAO = [
    'caralho',
    'merda'
]


TIPOS_IDENTIFICACAO = (
    ('CRM', 'CRM'),
    ('CREFITO', 'CREFITO'),
    ('CREF', 'CREF'),
)


class CaracteristicaQualitativa():
    PREFERENCIA = ['Agilidade', 'Atividade ao ar livre', 'Atividade em grupo', 'Constrole da respiração',
                   'Correção da postura', 'Flexibilidade', 'Ganho de massa muscular',
                   'Melhor condicionamento físico', 'Melhor flexibilidade', 'Melhor respiração', 'Perda de peso', 'Reflexo',
                   'Trabalha com todo o corpo']
    DOENCA = ['Não há', 'Asma', 'Diabetes', 'Obesidade', 'Pressão alta']
    DIFICULDADE_MOTORA = ['Não há', 'Problema na articulação das pernas', 'Problema na articulação dos braços',
                          'Paraplégico', 'Problemas no joelho', 'Hérnia de disco']
    MALEFICIO = ['Não há', 'Alto impacto', 'Bolada', 'Desgaste articulação dos braços', 'Desgaste articulação das pernas',
                 'Fortes pancadas no corpo', 'Lesões', 'Problemas nos calcanhares']


class tipoCaracteristica(IntEnum):
    PREFERENCIA = 0
    ALTURA = 1
    PESO = 2
    DOENCA = 3
    DIFICULDADE_MOTORA = 4
    MALEFICIO = 6
    NAO_HA = 10


class ValorCaracteristica(enum.Enum):
    PREFERENCIA = 0
    ALTURA = 1
    PESO = 3
    DOENCA = 5
    DIFICULDADE_MOTORA = 5
    MALEFICIO = 6
    NAO_HA = 10