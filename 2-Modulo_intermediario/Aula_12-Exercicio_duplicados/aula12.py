'''
Encontrar o primeiro número a ser duplicado em uma lista mestre que contém 12 listas
com números aleatórios de 1 a 10
'''
import random


def lists_generate(lst):  # Gerador de dados na lista
    for x in range(12):
        lista = []
        for n in range(10):
            lista.append(random.randint(1,10))
        lst.append(lista)


def fdoubles_valid(lista):  # Validador de primeiros números que se repetem
    cont = 0
    for x in range(12):
        if len(set(lista[cont])) < 10:
            valid_list = []  # Lista de "memória" dos argumentos que já foram verificados
            for n in lista[cont]:
                if not n in valid_list:
                    valid_list.append(n)
                else:
                    valid_list.append(n)
                    break
            print(f'{lista[cont]} - {valid_list[-1]} foi o primeiro número a se repetir.')
        else:
            print(f'{lista[cont]} - Não houve repetição!')
        cont += 1


# Execução do código

lista_mestre = []
lists_generate(lista_mestre)
fdoubles_valid(lista_mestre)

