'''
Entrada de dados em Python
'''

# Função input()

'''
Ao utilizar a função input() o tipo de dado sempre será uma string, por mais que coloque-se um número
no input
'''
'''
nome = input('Qual seu nome? ')
idade = input('Qual é a sua idade? ')
ano_nascimento = 2020 - int(idade)

print()
print(f'{nome} tem {idade} anos pois nasceu no ano de {ano_nascimento}')
'''

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

print()
print(f'O resultado da sua soma é: {num_1 + num_2}')

