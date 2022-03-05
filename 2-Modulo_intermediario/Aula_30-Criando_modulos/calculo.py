'''
Calculos do projeto app 1.0.0
'''
from random import randint as aleatorio

def exponencial(n1, n2):
    return n1 ** n2


def soma_tudo(array):
    ac = 0
    for n in array:
        ac += n
    return ac


list_generator = [round(x * 2 / 3) for x in range(aleatorio(1, 1000))]

if __name__ == '__main__':
    print(list_generator)
    print(soma_tudo(list_generator))
    print(exponencial(2, 10))
