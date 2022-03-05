'''
Parametros mutáveis em funções tem um problema
'''

'''
# Problema:

def show_lists(iteravel, lista=[]):
    lista.extend(iteravel)
    return lista


clientes1 = show_lists(['Antony', 'Joseph', 'Mary'])
clientes2 = show_lists(['Michael', 'Arlindo', 'Messias'])
clientes3 = show_lists(['Helio', 'Alfredo', 'Joilson'])

print(clientes1)  # Imprime a lista de todos os clientes (1, 2 e 3)
print(clientes2)  # Imprime a lista de todos os clientes (1, 2 e 3)
'''

'''
# Possível solução

def show_lists(iteravel, lista=None):
    if lista == None:
        lista=[]
    lista.extend(iteravel)
    return lista


clientes1 = show_lists(['Antony', 'Joseph', 'Mary'])
clientes2 = show_lists(['Michael', 'Arlindo', 'Messias'])
clientes3 = show_lists(['Helio', 'Alfredo', 'Joilson'])

print(clientes1)  # Imprime a lista de todos os clientes (1, 2 e 3)
print(clientes2)  # Imprime a lista de todos os clientes (1, 2 e 3)
'''