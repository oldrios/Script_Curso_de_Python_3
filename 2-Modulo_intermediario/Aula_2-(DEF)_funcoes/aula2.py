'''
Funções (def) em Python - return - (parte 2)
'''

# Atribuindo uma função para uma função

def f(var):
    return var


def f2():
    return f


variavel = f2()('Algum valor')

print(variavel, id(variavel), id(f))


