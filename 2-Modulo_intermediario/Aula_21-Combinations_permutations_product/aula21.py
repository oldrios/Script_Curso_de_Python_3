'''
Combinations, permutation e product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''

from itertools import combinations, permutations, product

pessoas = ['Ana', 'João', 'Marcos', 'Luis', 'Oldaque', 'Marcela', 'Larissa']

# Combinações
#for combinacao in combinations(pessoas, 2):
#    print(combinacao)

# Permutações
#for combinacao in permutations(pessoas, 2):
#    print(combinacao)

# Produto
for combinacao in product(pessoas, repeat=3):
    print(combinacao)

