'''
Desempacotamento de listas
'''

lista = ['Value 1', 'Value 2', 'Value 3',1,2,3,4,5,6,7,8,9,10,12,1000]

v1, v2, v3, *outra_lista, ultimo_da_lista = lista

print(outra_lista)