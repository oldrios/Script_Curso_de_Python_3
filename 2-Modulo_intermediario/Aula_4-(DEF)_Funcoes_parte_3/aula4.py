'''
Funções em Python - Args e Kwargs
'''

def funcao(*args, **kwargs):  # Utilizando o * antes do argumento, defininimos que a quantidade de parametros é indefinida
    print(args)
    print(kwargs)

    nome = kwargs.get('nome')
    idade = kwargs.get('idade')

    if nome or idade is not None:
        print(nome, idade)


lista = [1, 2, 3, 4 , 5, 6]
lista2 = [300, 400, 500, 600]

funcao(*lista, *lista2)  # Dessa forma desempacotamos e incluimos cada valor da lista em indices diferentes da tupla
funcao(lista, lista2)  # Dessa forma incluimos duas listas e cada indice de uma tupla
funcao(*lista, *lista2, nome='Oldaque', idade=25)  # Quando nomeamos os argumentos, eles exibem como uma KeyWords Args
funcao(lista, lista2, nome='Oldaque', idade=25)  # Os KeyWords Arguments são definidos com dois ** quando definimos função


