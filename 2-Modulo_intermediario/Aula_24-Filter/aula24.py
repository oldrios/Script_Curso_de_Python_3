from dados1 import produtos, pessoas, lista


'''
Estrutura da função filter()
variavel = filter(função, iterável)
Só é possível "filtrar" um dado do tipo iterável
'''

'''
# Aplicando filtro em listas

maior_que_5 = filter(lambda x: x > 5, lista)  # Utilizando lambda

print(set(maior_que_5))
'''


# Aplicando filtro em dicionários

def filtra_jovem(a):

    f'''Filtra só quem é jovi, meu jovi\n
    Então quer dizer que se sua idade estiver\n
    entre 16 e 30 anos, parabens, você é jovi'''

    if a['Idade'] >= 16 and a['Idade'] <= 30:
        a['É jovi'] = 'Verdade'
        return True


maior_que_5 = filter(filtra_jovem, pessoas)  # Utilizando função

filtra_jovem()

for n in maior_que_5:
    print(n)

