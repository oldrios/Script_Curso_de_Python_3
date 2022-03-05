'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''


vetor = list(range(1, 21))
par = []
impar = []


for valor in vetor:
    par.append(valor) if valor % 2 == 0 else impar.append(valor)


print(f'Vetor completo: {vetor}')
print(f'Vetor par: {par}')
print(f'Vetor ímpar: {impar}')

