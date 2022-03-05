'''
-   Criar variáveis para nome(str), idade(int),
    altura (float) e peso (float) de uma pessoa
-   Criar variável com o ano atual (int)
-   Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
-   Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
-   Exibir um texto com todos os valores na tela usando f-strings (com as chaves)
'''

nome = 'Larissa'
idade = 21
altura = 1.72
peso = 66.0
imc = peso / altura ** 2
ano_atual = 2019
ano_nascimento = ano_atual - idade

print('{n} tem {i} anos, {a} de altura e pesa {p}kg.'.format(n=nome, i=idade, p=peso, a=altura))
print('O IMC de {n} é {i:.2f}.'.format(i=imc, n=nome))
print('Larissa nasceu em {a}.'.format(a=ano_nascimento))