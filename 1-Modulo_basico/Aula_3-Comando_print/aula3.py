# No Python, toda estrutura com 'exemplo()' é uma função

# print(123456)  # Função print sem a virgula
# print('Oldaque','Rios','Neto')  # A função print adiciona um espaço a cada parâmetro imputado dentro do parêntese
# print('Oldaque', 'Rios', sep='-')  # Podemos definir um separador que não seja o padrão, que nesse caso é o espaço
# print('Curso','de','Python', sep='_',end='$$$')  # Ao colocar o parâmetro 'end=' é determinado como a função terminará
# print('Curso','de','Python', sep='_',end='')
# O parâmetro 'end=' se não for definido, a função quebrará a linha e exibe o outro proximo comando em baixo

#Print('Curso','De','Python')
'''O Python diferencia letras maíusculas de minúsculas, ou seja ao tentar
mandar esse comando com a primeira letra maíuscula, aparece erro'''

# Exercicio 1, definir o CPF 824.176.070-18 com função print e parametros SEP e END

# Forma 1
print('824','176','070',sep='.', end='-18')
print('')  # Quebrar a linha
# Forma 2
print('824','176','070',sep='.', end='-')
print('18')


