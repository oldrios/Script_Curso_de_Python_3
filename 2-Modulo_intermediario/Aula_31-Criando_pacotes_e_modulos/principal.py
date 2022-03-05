'''
Como criar os nosso próprios pacotes em Python
'''

from vendas.calc_preco import desconto, aumento
from vendas.formata import precos

'''
preco = input('Digite o preco do produto: ')
desc = input('Qual o valor (em %) que deseja aplicar o desconto: ')
preco_desconto = desconto(preco, desc)
if preco == None or desc == None:
    print('Erro. Você não digitou números! Tente novamente')
else:
    print(f'O valor com o desconto é {preco_desconto}')
'''

lista_precos = [300, 40.50, 49.99, 25.34]


for n in lista_precos:
    print(desconto(n, 15))

for n in lista_precos:
    print(precos.percentual(n))


