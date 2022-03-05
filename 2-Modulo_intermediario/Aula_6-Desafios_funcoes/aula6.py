'''
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
'''

'''
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a função1 executar duas funções que recebam um número diferente de argumentos.
'''

'''
# Resolução exercício 1

def funcao1(nome):
    return f'Olá {nome}'

def funcao2(a):
    var = funcao1(a)
    return var

variavel = funcao2('Juvenal')

print(variavel)
'''

# Resolução exercicio 2

def saudacao(arg):
    return f'Olá! {arg}'

def nome(arg):
    return f'fiquei sabendo que seu nome é {arg}'

def nome_saudacao(arg1, arg2):
    return f'{saudacao(arg1)}, {nome(arg2)}'

variavel = nome_saudacao('Boa noite', 'Maria')

print((variavel))



