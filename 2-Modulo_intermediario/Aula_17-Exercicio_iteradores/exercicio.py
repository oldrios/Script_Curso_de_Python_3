'''
Somar os valores de um carrinho de compras onde cada produto
pode ter uma variação no preço
'''
import sys

# Gerador de produtos e valor
pp_generator = [('Produto ' + str(int(x / 10)), x + 20) for x in range(10, 150, 10)]

# Carrinho recebe os produtos e valores
carrinho = [x for x in pp_generator]
print(type(carrinho), carrinho)

# Total da compra
total_compra = [v for p, v in carrinho]
print(type(total_compra), sum(total_compra))



