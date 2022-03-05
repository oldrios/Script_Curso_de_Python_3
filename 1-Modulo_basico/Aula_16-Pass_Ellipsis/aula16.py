'''
Cláusulas Pass e Ellipsis
Quando estamos escrevendo um código e não queremos colocar um comentário
para evitar que dê algum erro de sintaxe/indentation utilizamos o pass ou ellipsis
para lembrar que precisamos terminar de escrever aquele código, exemplos abaixo
'''


variavel = True

# Ellipsis

if variavel:
    ...  # Aqui está uma ellipsis
else:
    print('Go')

# Pass

if variavel:
    pass
else:
    print('Go')
