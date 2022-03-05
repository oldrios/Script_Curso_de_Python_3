'''
Geradores, iteradores e iteráveis em Python

Objetos iteráveis não são iterados por natureza, precisam de um iterador para serem "separados".

'''

'''
lista = 'string'
lista = ['a', 'b', 'c', 'd']



lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(hasattr(lista, '__next__'))
'''

import sys
import time

'''
# Método 1 para criar um Gerador

def gerador():
    for n in range(100):
        yield n
        time.sleep(0.2)


lista = gerador()

for v in lista:
    print(v)
'''

'''
Para processar uma grande quantidade de dados o mais correto é se usar um gerador 
pois a quantidade de bytes processados por vez é infinitamente inferior a uma lista
pois a lista processa todos os dados de uma lista por vez 


l1 = [x for x in range(1000000)]
l2 = (x for x in range(1000000))  # Quantidade de dados semelhantes ao l1

print(f'Tamanho da l1 = {sys.getsizeof(l1)} bytes / Tipo da l1 = {type(l1)}')  # Tamanho da l1 = 8697456 bytes
print(f'Tamanho da l2 = {sys.getsizeof(l2)} bytes / Tipo da l2 = {type(l2)}')  # Tamanho da l2 = 112 bytes



print(l1[99])
'''

string = 'Oldaque Rios'
iterador = iter(string)

try:
    print(next(iterador))  # O
    print(next(iterador))  # l
    print(next(iterador))  # d
    print(next(iterador))  # a
    print(next(iterador))  # q
    print(next(iterador))  # u
    print(next(iterador))  # e
    print(next(iterador))  #
    print(next(iterador))  # R
#    print(next(iterador))  # i
#    print(next(iterador))  # o
#    print(next(iterador))  # s
#    print(next(iterador))  # Erro (há mais comando para iteração do que itens no iterador)
#    print(next(iterador))  # Erro (há mais comando para iteração do que itens no iterador)
#    print(next(iterador))  # Erro (há mais comando para iteração do que itens no iterador)
except:
    pass

print('Acabou o next')

for letra in iterador:
    print(letra)



