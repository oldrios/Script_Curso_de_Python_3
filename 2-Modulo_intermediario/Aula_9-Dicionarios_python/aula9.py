'''
Dicionarios em Python
Dicionarios em Python criam uma refêrencia personalizada (chave/key) para o index dos dados que são inseridos
dentro de uma tupla com chave e valor.
'''

'''
cadastro = {'Nome' : 'Oldaque', 'Peso' : 64.5, 'Idade' : 24}
cadastro['Sexo'] = 'M'

print(cadastro, type(cadastro))
print(cadastro.items())
print(cadastro.keys())
print(cadastro.values())

for k, v in cadastro.items():
    print(f'{k}: {v}')
    
'''

'''
uniao = []
uf1 = {'Estado' : 'Minas Gerais', 'UF' : 'MG'}
uf2 = {'Estado' : 'Bahia', 'UF' : 'BA'}
uf3 = {'Estado' : 'Piaui', 'UF' : 'PI'}

uniao.append(uf1)
uniao.append(uf2)
uniao.append(uf3)

print(uniao)

for n in uniao:
    for k, v in n.items():
        print(f'{k}: {v}')
'''

'''

uniao = list()
state = dict()

for l in range(3):
    state['Estado'] = str(input('Digite qual estado: '))
    state['UF'] = str(input('Digite a UF: '))
    uniao.append(state.copy())

for n in uniao:
    for k, v in n.items():
        print(f'{k}: {v}')
'''

'''
clientes = {
    'cliente_1' : {
        'Nome' : 'Armando',
        'Sobrenome' : 'Junior',
        'Idade' : 39
    },
    'cliente_2' : {
        'Nome' : 'Wilson',
        'Sobrenome' : 'Morais',
        'Idade' : 56
    },
    'cliente_3' : {
        'Nome' : 'Jessica',
        'Sobrenome' : 'Arruda',
        'Idade' : 25
    },
    'cliente_4' : {
        'Nome' : 'Ana Julia',
        'Sobrenome' : 'Gonçalves',
        'Idade' : 20
    }

}

for cliente_k, cliente_v in clientes.items():
    print('~' * 40)
    print(f'\tEsse é o cliente {cliente_k}')
    for chave, valor in cliente_v.items():
        print(f'\t\t{chave}: {valor}')
    print('-' * 40)
    print()
'''

'''
# Copiando o valor de um dicionário para uma variável sem alterar o dicionário

import copy


dict1 = {1 : 'Valor', 2 : 'Another value', 3 : 'Mais um valor', 'nomes' : ['Antonio', 'Rios']}
# v = dict1  # Dessa forma linkamos a variável ao dicionario e toda alteração na variável afetará o dicionário
# v = dict1.copy()  # Assim criamos uma ref. com o dicionario e dado que não estivere dentro de lista não é alterado
v = copy.deepcopy(dict1)  # Dessa forma, nem dados que estiverem dentro de listas serão alterados no dicionario

v[2] = 'Same value'
v['nomes'][0] = 'Nidnha'

print(dict1)
print(v)
'''

'''
# Deletando valores de um dicionário

d1 = {
    'Id' : 8374,
    'Tipo' : 'Venda',
    'Valor' : 23123,
    'User' : 'jkl234s'
}
print(d1)

d1.pop('Tipo')  # Assim indicamos qual chave será excluída
print(d1)

d1.popitem()  # Assim excluimos o último item do dicionário
print(d1)
'''

'''
# "Concatenando" dois dicionários

dict1 = {
    'Id' : 8374,
    'Tipo' : 'Venda',
    'Valor' : 23123,
    'User' : 'jkl234s'
}

dict2 = {
    1 : 850,
    2 : 3847,
    3 : 7645
}

dict1.update(dict2)


print(dict1)
print(dict2)
'''




