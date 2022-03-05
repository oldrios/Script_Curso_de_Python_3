'''
Formatando valores com modificadores

:s - formata texto (string)
:d - formata números inteiros (int)
:f - formata números decimais (float)
:.(número)f - QUantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade máxima de caracteres)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

# Exemplo de formatação para preenchimento com definição de quantidade de caracteres

# Caracteres a esquerdas
var = 22

print(f'{var:0>10}')

# Caracteres ao centro
var_2 = 765

print(f'{var_2:0^10}')

# Caracteres a direita
var = 33

print(f'{var:0<10}')

# Unindo os tipos de formatação (Definindo qtd de caracter + casas decimais)
var_3 = 45

print(f'{var:0>10.2f}')

# Utilizando definição de quantidade de caracter com strings
nome = 'Oldaque Rios'

print(f'{nome:#^30}')

# Utilizando tipo de formatação com strings

nome_sobrenome = 'Oldaque RiOs NeTO'
texto = 'HOJE ESTAMOS em uma situação Complicada galera! Estamos em pandemia muleque'

print(f'{nome_sobrenome.lower()}')  # tudo minúsculo
print(f'{nome_sobrenome.upper()}')  # TUDO MAIÚSCULO
print(f'{nome_sobrenome.title()}')  # Primeiras Letras Maiúsculas


print(f'{texto.capitalize()}')  # Primeiras letras maiúsculas, restante é minúscula



