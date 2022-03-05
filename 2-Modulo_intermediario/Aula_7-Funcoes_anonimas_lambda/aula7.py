'''
Expressões anonimas - Lambda
'''
'''
lista = [
    ['ID1', 50],
    ['ID2', 35],
    ['ID3', 15],
    ['ID4', 20],
    ['ID5', 30]
]

lista.sort(key=lambda c: c[1], reverse=True)

print(lista)

'''
'''
A lambda é extremamente útil quando precisamos utilizar as propriedades que uma função têm
mas que não necessariamente será uma "rotina" no nosso código. Ou seja, para que tenhamos funções 
que estarão bem definidas no códig não se "misturem" com funções que podemos por exemplo utilizar uma
só vez.
'''


import random


lista1 = []
lista2 = []
estatistica = []


def adcvalor(l1):
    lista1.append(random.randint(1, l1))
    lista2.append(random.randint(1, l1))


comparativo = lambda l1, l2: l1[-1] == l2[-1]



for n in range(10):

    c = 1
    adcvalor(100)
    while comparativo(lista1, lista2) == False:
        print(f'{c} tentativa(s), o valor não bateu')
        print(lista1, lista2)
        del(lista1[0])
        del(lista2[0])
        adcvalor(100)
        c += 1

    else:
        print(f'{c} tentativa(s), o valor bateu!')
        print(lista1, lista2)
        lista_temp = []
        lista_temp.append(lista1[:])
        lista_temp.append(c)
        estatistica.insert(-1, lista_temp[:])
        del(lista_temp)

    del(lista1[0])
    del(lista2[0])



print(f'Combinação concluida! Ao todo tivemos {len(estatistica)} combinações!')
print(estatistica)
