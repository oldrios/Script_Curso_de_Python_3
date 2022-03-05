'''
Fazer um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}

aluno['nome'] = input('Informe o seu nome: ')
aluno['media'] = input(f'Certo {aluno["nome"]}, agora informe a sua média: ')
aluno['media'] = float(aluno['media'])

if aluno['media'] > 6:
    print(f'Muito bem {aluno["nome"]} você está aprovado!')
else:
    print(f'É uma pena {aluno["nome"]} você não está aprovado. :/')

