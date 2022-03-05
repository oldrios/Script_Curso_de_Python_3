'''
Split, Join, Enumerate
- Split: Dividir uma string
- Join: Juntar uma lista # str
- Enumerate: Enumerar elementos da lista # iteráveis
'''

'''
string = 'todo mundo sabe que todo mundo não sabe de nada todo'

lista1 = string.split(' ')
lista2 = string.split(',')

c = 0
palavra = ''

for valor in lista1:
    qtd_de_vezes = lista1.count(valor)

    if c < qtd_de_vezes:
        c = qtd_de_vezes
        palavra = valor

print(f'A palavra "{palavra}" apareceu {qtd_de_vezes}x - Sendo assim apareceu mais vezes.')
'''

'''
texto = 'Nada pode me separar de você'
lista1 = texto.split(' ')
texto2 = ','.join(lista1)

print(texto)
print(lista1)
print(texto2)
'''

'''
texto = 'Nada pode me separar de você'
lista1 = texto.split(' ')

for indice, valor in enumerate(lista1):
    print(indice, lista1[indice])
    # Outro método
    # print(indice, valor)
'''
'''
# Criando listas dentro de uma lista

listas = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for indice, valor in enumerate(listas):
    print(indice, valor)


listas = [
    [0, 'Value 1'],
    [1, 'Value 2'],
    [2, 'Value 3'],
]

for indice, valor in listas:
    print(indice, valor)


listas = ['Value 1', 'Value 2', 'Value 3']

n1, n2, n3 = listas

print(n1, n3, n2)
'''



