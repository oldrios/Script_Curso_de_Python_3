'''

Relacionamento de classes

Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É

'''
from classes import ClienteVIP, Cliente, Aluno, Pessoa

c1 = Cliente('Jovem', 20)
a1 = Aluno('Suelen', 15)
p1 = Pessoa('Outro', 29)
c2 = ClienteVIP('Karin', 24, 'Premium Line')

print(c1.nome, c1.idade)
c1.falar()
c1.comprar()
print()

print(c2.nome, c2.idade, c2.classification)
c2.outra_fala()
print()




