
'''
# Formato 1 (versão extendida)

# begin

nome = input('Digite seu nome: ')

if nome:
    print(nome)
else:
    print('Você não digitou nada jovem.')

# end
'''

'''
# Formato 2 (encurtado com operador OR)

# begin

nome = input('Digite seu nome: ')

print(nome or 'Você não digitou nada o.o')

# end
'''

'''
# Ignorando valores falsos com or

# begin
a = ''
b = None
c = False
d = []
e = ()
f = {}
g = 4
h = 'str'

variavel = a or b or c or d or e or f or h or g

print(variavel)
# end
'''

'''
Utilizando o operador OR em uma expressão lógica será considerado para a saida o primeiro valor 
booleano verdadeiro (True), lembrando que é analisado da esquerda para a direita
'''



