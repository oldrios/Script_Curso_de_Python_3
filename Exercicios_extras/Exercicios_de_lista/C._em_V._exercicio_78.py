'''
Faça um programa que leia 5 valores e guarde-os em uma lista.

No final mostre qual foi o maior e menor valor digitados e suas respectivas posições.
'''
'''
# Inicio
lista = list(range(3,12,2))



menor = 0
maior = 0

for valor, l1 in enumerate(lista):
    if l1 == max(lista):
        menor = l1
        print(f'O maior valor é o {menor}, está na posição {valor}')

    elif l1 == min(lista):
        maior = l1
        print(f'O menor valor é o {menor}, está na posição {valor}')

# Fim
'''


'''
Crie um progrma onde o usuário possa digitar vários valores numéricos e cadastre-os 
em uma lista. Caso o número já esteja na lista ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
# Inicio

lista = []
lista_temporaria = []

opcao = input('Deseja inserir um valor numerico na lista? [s]im ou [n]ão: ')

while opcao.lower() == 'sim' or opcao.lower() == 's':

    lista_temporaria.append(input('Digite um valor para inserir na lista: '))
    if not lista_temporaria[-1] in lista:
        lista.append(lista_temporaria[-1])
    else:
        print('Você não pode repetir os valores, digite outro valor.')
        continue

    if not lista[-1].isdigit():
        print(f'"{lista[-1]}" não é permitido, digite apenas numeros inteiros!')
        lista.pop()
        continue
    opcao = input('Deseja inserir outro valor? [s]im ou [n]ão: ').lower()
    continue

# Transformando em inteiro para ordem crescente valer para números e não strings
lista_temporaria = []

for numero in lista:
    if numero.isdigit():
        lista_temporaria.append(int(numero))


lista_temporaria.sort()
print('-======-======-======-======-======-======-======-======-======-======-======-======-')
print('Sua lista é:')
print(lista_temporaria)

# Fim




