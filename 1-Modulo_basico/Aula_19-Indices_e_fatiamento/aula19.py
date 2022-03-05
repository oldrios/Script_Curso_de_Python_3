'''
Manipulando strings - Aula 06
- Strings indices
- Fatiamento de strings [início:fim:passo]
- Funções built-in len, abs, type, print e etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''


# Indices

# Positivo   [012345678]
nome =      'Python s2'
#Negativo  -[987654321]

# Delimitando até onde irá a string com o indice [inicio 0 : fim 6]
new_nome = nome[0:6]

# Ao definir um indice fim, ele irá até o indice informado e não trará o indice fim
# Exemplo, ao colocar o indice [0:6] ele trará da primeira letra (indice inicio 0)
# e o último caracater será o 5 (indice fim 6)

print(new_nome)


