'''
Manipulando arquivos - Lendo, escrevendo e criando
'''

'''
file = open('teste1.txt', 'w+')  # Método de abertura/criação de um arquivo
file.write('Pois e malandro, linha 1\n')  # Inserindo linhas no arquivo
file.write('Pois e malandro, linha 2\n')
file.write('Pois e malandro, linha 3\n')
file.write('Pois e malandro, linha 4\n')
file.write('Pois e malandro, linha 5\n')
file.write('Pois e malandro, linha 6\n')
file.write('Pois e malandro, linha 7\n')

# Métodos de leitura

file.seek(0, 0)  # Retornando para o início do arquivo
print(file.readline(), end='')  # Lendo linha por linha
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline())
print('_=' * 25, '\n')

file.seek(0, 0)
print(file.read())  # Lendo o arquivo inteiro
print('_=' * 25, '\n')

file.seek(0, 0)
print(file.readlines()) # Traz todas as linhas como uma lista
print('_=' * 25, '\n')

file.seek(0, 0)
for n in file:
    print(n, end='')
print('\n', '_=' * 25, '\n')

file.close()
'''

'''
# Estrutura de manipulação de arquivos em outras linguagens de programação

try:
    file = open('teste1.txt', 'w+')
    file.write('Pois e malandro, linha 1\n')
    file.write('Pois e malandro, linha 2\n')
    file.write('Pois e malandro, linha 3\n')
    file.seek(0)
    print(file.read())
finally:
    file.close()
'''
import os
# Estrutura de manipulação de arquivos Pythonica

with open('teste1.txt', 'w+') as file:
    file.write('Pois e malandro, linha 1\n')
    file.write('Pois e malandro, linha 2\n')
    file.write('Pois e malandro, linha 3\n')

    file.seek(0)
    print(file.read())

os.remove('teste1.txt')



