'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

'''
var = 10

# Índices das listas

# Positivos    0    1    2    3   4     5    6
lista =      ['A', 'B', 'C', 'D', True, 7.3, var]
# Negativos    -7   -6   -5   -4  -3    -2   -1
'''

'''
print(lista)
print(lista[3])
print(lista[::2])
'''

'''

# Concatenando listas


# Primeira forma
l1 = [1, 2 , 3]
l2 = [4, 5 , 6]
l3 = l1 + l2


# Segunda forma
l1 = [1, 2 , 3]
l2 = [4, 5 , 6]
l1.extend(l2)

print(l1)
print(l2)

'''

'''
# Inserindo valores em lista


# Utilizando função .extend() (não recomendável)

l1 = [1, 2 , 3]
l1.extend('a')

# Utilizando função .append() (recomendável)

l1 = [1, 2 , 3]
l2 = [4, 5 , 6]
l2.append('l2 aqui')

# Utilizando a função insert(indíce, valor) (recomendável)

l2 = [4, 5 , 6]
l2.insert(0, 'Churros')  # Dessa forma, o índice determina a posição do valor inserido

print(l2[0])

print(l2)
'''

'''
# Deletando um valor da lista

# Função .pop(indice)

l1 = [1, 2 , 3]
print(l1)

l1.insert(3, 'churros')
print(l1)

l1.pop(1)
print(l1)




# Utilizando função .del(variavel[indice])

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
var = input('Digite um valor ele aparecerá logo no começo da lista: ')
l2.insert(0, var)
print(l2)
del(l2[0])
print(l2)
del(l2[0:2])
print(l2)

'''

'''
# Projetando minimos e máximos da lista

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(min(l2))
print(max(l2))

'''

'''
# Somando todos valores da lista

l2 = [3, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = list(range(0,10))
soma = 0

for n in enumerate(l2):
    print(n)

for valor in l2:
    soma += valor

print (soma)
'''

'''
l2 = ['texto', True, 2, -86.4]



for elem in l2:
    print(f'O elemento é "{elem}" e é classificado com o tipo: {type(elem)}')
'''


secreto = 'juazeiro'
palavras_digitadas = []
chances = 3
dica = input('Antes de começar, digite uma dica: ')



while True:
    if chances <= 0:
        print('Agora não restam mais chances, você está eliminado(a)!')
        break

    print(f'Você tem {chances} chance(s).')
    print(f'Sua dica é "{dica}".')
    print(f'Sua palavra tem {len(secreto)} letras')
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Estou de olho! Digite apenas uma letra. Perdeu uma chance!')
        chances -= 1
        continue
    if letra in palavras_digitadas:
        print('Epa, você já digitou essa letra, não se lembra?')
        continue

    palavras_digitadas.append(letra)

    if letra in secreto:
            print(f'AEE, a letra "{letra}" existe na palavra secreta')
    else:
            print(f'IIH, A letra "{letra}" não está na palavra secreta! Perdeu uma chance!')
            palavras_digitadas.pop()
            chances -= 1

    palavra_temporaria = ''
    for letra_secreta in secreto:
        if letra_secreta in palavras_digitadas:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '_'

    if palavra_temporaria == secreto:
        print(f'VOCÊ GANHOU!! PARABÉNS A PALAVRA SECRETA ERA {secreto}')
        break
    else:
        print(f'Palavra formada até o momento: {palavra_temporaria}')
        print()








