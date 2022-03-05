'''
Groupby em Python - Agrupando valores
'''
from itertools import groupby, tee

alunos = [
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Marcio', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Amanda', 'nota': 'B'},
    {'nome': 'Beatriz', 'nota': 'C'},
    {'nome': 'Beatriz', 'nota': 'C'},
    {'nome': 'Beatriz', 'nota': 'C'},
    {'nome': 'Ramon', 'nota': 'B'},
    {'nome': 'Ramon', 'nota': 'B'},
    {'nome': 'Ramon', 'nota': 'B'},
    {'nome': 'Ramon', 'nota': 'B'},
    {'nome': 'Alves', 'nota': 'C'},
    {'nome': 'Robson', 'nota': 'A'},
    {'nome': 'Geralda', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'D'},
]

ordena = lambda item: item['nota']

# Ordenando com a função sorted()
alunos.sort(key=ordena)


alunos_group = groupby(alunos, ordena)

for nota_agrupamento, alunos_agrupados in alunos_group:
    v1, v2 = tee(alunos_agrupados)

    print(f'Agrupamento da nota: {nota_agrupamento}')
    for aluno in v1:
        print(f'\t\t{aluno}')
    qtd_aluno = len(list(v2))
    print(f'\t{qtd_aluno} alunos tiraram a nota {nota_agrupamento}')
    print('=-' * 30)

    print()
