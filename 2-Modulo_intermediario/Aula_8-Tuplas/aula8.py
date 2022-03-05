'''
Tuplas em Python
São parecidas com as listas porém uma Tupla não é alterável, ou seja
os intens dentro de uma Tupla não são mutáveis e não podem sofrer
alteração, conseguimos adicionar um novo valor a uma Tupla porém
ela segue numa ordem de crescimento adicionando valores sempre na última
posição.
'''

'''
t1 = (1, 2, 3)

t2 = ('Conditions', 'Are not True', 'Yeaaaah')

t3 = t1 + t2

# Desempacotando uma Tupla

n1, n2, n3, n4, *_ = t3


print(t3)

'''

# Método para alterar valor de uma tupla

t1 = ('Bob', 'I Wanna Luv ya', 'Rastaffari', 'Dont worry, be happy', 'Legalizeeeee')
t1 = list(t1)
t1[3] = 'Alter the changeeeee'
t1 = tuple(t1)

print(t1)
