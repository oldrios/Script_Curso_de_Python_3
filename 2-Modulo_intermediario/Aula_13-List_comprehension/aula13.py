'''
List Comprehension em Python
São automações que utilizando condições e laçaos em uma única linha
para montar uma lista
'''

l1 = list(range(100))
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

ex1 = [variavel for variavel in l1]
ex2 = [v * v for v in l1]  # Elevação de cada elemento da l1 ao quadrado
ex3 = [(a, b) for a in l2 for b in range(2)]  # Criando tuplas com 'Coordenadas' de 0 a 1

l3 = ['Jovem', 'Maiscedo', 'Otimo', 'Isso ai', 'Abracadabra']
ex4 = [v.replace('a', '@').upper() for v in l3]  # Substitui a por @ e coloca todas as letras maíusculas

tupla = (
    ('Chave1', 'Valor1'),
    ('Chave2', 'Valor2'),
    ('Chave3', 'Valor3'),
)
ex5 = [(b, a) for a, b in tupla]
ex5 = dict(ex5)

ex6 = [v for v in l1 if v % 2 == 0]
ex6 = [v for v in l1 if v % 2 == 0 if v % 5 == 0]


ex7 = [v if v % 3 == 0 else ',' for v in l1]
ex7 = [v if v > 9 and v % 8 == 0 else ',' for v in l1]



print(ex7)



