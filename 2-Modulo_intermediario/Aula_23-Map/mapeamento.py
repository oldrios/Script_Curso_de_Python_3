from dados import produtos, pessoas, lista

'''
Estrutura da função map()
variavel = map(função, iterável)
Só é possível "mapear" um dado do tipo iterável
'''

'''
nova_lista = map(lambda x: x + 10, lista)

comprehensions = [x + 10 for x in lista]
print(comprehensions)
print(lista)
print(list(nova_lista))

'''
'''
# Iterando dicionarios com a função map


def troca_letra(n):
    n['nome'] = n['nome'] + ' Sbrenme'
    if 'O' in n['nome']:
        n['validacao'] = 'Tem O aqui.'  # Adicionando nova chave e valor ao dicionario
    else:
        n['validacao'] = 'Não tem O aqui.'
    return n


sobrenome = map(troca_letra, pessoas)

for pessoa in sobrenome:
    print(pessoa)
'''



