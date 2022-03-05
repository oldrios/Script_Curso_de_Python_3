'''
str = string
'''

''' No Python temos uma tipagem dinâmica de dados, ou seja, ele ao identificar uma aspa por exemplo
ele irá procurar outra aspa para finalizar o comando, pois o tipo desse dado seria uma
string. Obs Se a string começar com aspa simples o identificador dinâmico irá procurar 
outra aspa simples para terminar o código, se por acaso for uma aspa dupla, o identificador também 
irá procurar uma aspa dupla para finalizar o comando'''

# Exemplo de como NÃO fazer uma string

'''print('Essa é uma 'string'(str).')'''

# Um dos metódos que podemos utilizar é diferenciar as aspas dentro da string para não confundir o identificador

print('Essa é uma "string" (str).')
print("Essa é uma 'string' (str).")

# Um outro metódo é utilizar uma barra invertida para informar ao identificador que a string não termina na próxima aspa

print('Essa é um outro método de \'string\' (str).1')
print("Essa é um outro método de \"string\" (str).1")

# A forma mostrada acima não é tão aconselhável pois deixa o código 'sujo', porém dependendo da necessidade
# há a possibilidade de ser utilizado

# Utilizando a função print com uma barra invertida '\' dentro da string

print('Aqui teremos um texto com barra invertida \n, por exemplo - Metodo incorreto')


# Para evitar que o Python não quebre a linha quando usamos a barra invertida na string
# precisamos adicioar a letra 'r' antes das aspas da função print para que o identificador de tipo de dados
# do Python entenda que não é pra executar nenhum comando dentro da string, exemplo abaixo:

print(r'Aqui teremos um texto com barra invertda \n por exemplo - Metodo correto')


