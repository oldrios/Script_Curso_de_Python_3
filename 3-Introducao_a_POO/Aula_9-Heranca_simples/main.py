

'''

Relacionamento de classes

Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É

'''
from classes import Cliente, Aluno, Pessoa

c1 = Cliente('Jovem', 20)
a1 = Aluno('Suelen', 15)
p1 = Pessoa('Outro', 29)

print(c1.nome, c1.idade)
c1.falar()
c1.comprar()
print()

print(a1.nome, a1.idade)
a1.falar()
a1.estudar()
print()

print(p1.nome, p1.idade)
p1.falar()
print()


