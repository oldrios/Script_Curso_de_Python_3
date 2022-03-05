'''
Reduce em Python
'''

'''
Estrutura da função filter()
variavel = reduce((lambda var_inicial, variavel expressão: execução da função), iterável, valor var_inicial)
Só é possível fazer o reduce em um dado do tipo iterável
'''

from dados import produtos, pessoas, lista
from functools import reduce

# Acumulando valores

ac = 0
for n in lista:  # Método tradicional (muito utilizado em outras linguagens)
    ac += n

print(ac)


total = reduce(lambda ac, n: ac + n, lista, 0)  # Método utilizando reduce (reduz linhas de códigos)

print(total)

# Reduce com dicionários

soma_idade = reduce(lambda ac, i: i['Idade'] + ac, pessoas, 0)

print(round(soma_idade / len(pessoas)))  # Retorna a média das idades

