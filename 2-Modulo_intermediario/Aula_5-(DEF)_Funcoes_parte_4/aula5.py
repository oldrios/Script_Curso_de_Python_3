'''
Escopo de variáveis em Python

Escopo local e global
'''
'''
variavel = 'valor'  # Escopo global - É considerada a mesma para qualquer outro comando

def funcao():
    print(variavel)

def funcao2():
    variavel = 'Outro valor'  # Escopo local - Só altera a varíavel dentro da função
    print('-' * 2 *len(variavel))
    print(variavel)

def funcao3():
    global variavel  # Escopo global - Altera a variável em todo o seu código a partir daqui
    variavel = 'Outro valor'
    print('-' * 2 *len(variavel))
    print(variavel)

funcao()
funcao2()
# funcao3()  # Aqui mudamos a variavel global - ATENÇÃO NÃO RECOMENDÁVEL UTILIZAR ESSE MÉTODO
print(f'variavel é "{variavel}"')
'''

'''
Método para "passar" uma váriável de uma função para outra função
Como as variáveis locais só existem no seu comando (ex dentro da função A) não se pode por ventura
tentar linkar diretamente a variável dessa "função A" para uma nova "função B" que desejamos criar,
para isso podemo utilizar o método abaixo:
'''

def funcao():
    outra_variavel = 'valor'
    return outra_variavel  # Tratando o dado para inserção

def funcao2(arg):
    print(arg)

var = funcao()  # Atribuindo o valor da função para uma variável

funcao2(var)  # Atribuindo o valor da variável como argumento de uma função