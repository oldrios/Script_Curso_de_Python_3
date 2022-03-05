from classes import Cliente, Endereco

p1 = Cliente('Jovem', 19)
p1.insere_endereco('Manhattan', 'New York')
p1.insere_endereco('Campinas', 'São Paulo')
print(p1.nome, p1.idade)
p1.lista_endereco()
del (p1)
print()

p2 = Cliente('Ana', 23)
p2.insere_endereco('Goiania', 'Goiás')
print(p2.nome, p2.idade)
p2.lista_endereco()
del (p2)
print()

p3 = Cliente('Marcela', 28)
p3.insere_endereco('São Paulo', 'São Paulo')
p3.insere_endereco('Feira de Santana', 'Bahia')
print(p3.nome, p3.idade)
p3.lista_endereco()
del (p3)
print()

print('=-' * 40)


