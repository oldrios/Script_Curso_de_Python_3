'''
Tipos de dados
str - String/texto 'Assim' "Assim" <-Exemplos de string
int - Inteiro - 123456 - 0  - 10 - 100 - 90 - 85 - 34
float - real/decimal/ponto flutuante - 10.50 12.43 34.54 0.0
bool - booleano/lógico - True/False 10 == 10 -> true | 20 == 5 -> false
'''


# Utilizando a função Print(Type()), é retornado com a class referente ao tipo, nesse caso str ou string

# Tipos de dados String
print('Oldaque',type('Oldaque'))
print('10.4',type('10.4'))
''' Atenção, mesmo utilizando números, ao adicionar as aspas o identificador do Python 
considera que o tipo de dado é String'''

# Tipos de dados númericos - Int e Float
print(1,type(1))
print(10.4,type(10.4))



# Tipos de dados Booleanos - True or False
print(10==10,type(10==10))
print('L'=='l',type('L'=='l'))
print(bool('a'),type(bool('a')))
print(bool(''),type(bool('')))
print(bool(1),type(bool(1)))
print(bool(0),type(bool(0)))

# Alterando o tipo de dados

print('Oldaque', type('Oldaque'), bool('Oldaque'))
print('10', type('10'), type(int('10')))



# Exercicio

# String: nome
print('Oldaque', type('Oldaque'))

# Int: Idade
print(24, type(24))
idade = 24

# Float: Altura
print(float(1.70), type(1.70))

#  Booleano: Validar se é maior de idade
print(idade >= 18, type(idade >= 18))

