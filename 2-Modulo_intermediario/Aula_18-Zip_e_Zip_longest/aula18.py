'''
Zip - Unindo iteráveis
Zip_longest - Itertools
'''

from itertools import zip_longest

# Listas aleatórias

marca = ['Fiat', 'Land Rover', 'Jeep', 'Volkswagen', 'Toyota']
modelo = ['Toro', 'Discovery', 'Renegade', 'Golf']
potencia = [1.8, 2.5, 1.8, 2.0]

carro = zip_longest(
    marca,
    modelo,
    potencia,
    fillvalue='N/E'
)



for m, mo, p in carro:
    print(m, mo, p)
