'''
Realizar as seguintes transformações em uma string utilizando list comprehensions
'''

string = '0123456789012345678901234567890123456789012345678901234567890123456789'
lista = ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']
retorno = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'
max = 10

l1 = [string[id: id + max] for id in range(0, len(string), max)]


# Exercicio auto proposto

d3 = [f'Key_{x**2}' for x in range(256) if x % 4 == 0]  # Método mais usual
d4 = [v[:-3] + '.' + v[-3:] for v in d3 if len(v) > 7]
d5 = [v for v in d3 if len(v) < 7]
d6 = d5 + d4



