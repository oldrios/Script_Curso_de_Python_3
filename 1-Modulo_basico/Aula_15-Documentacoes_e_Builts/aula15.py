'''

Documentações e funções built-in https://docs.python.org/3/library/stdtypes.html

Funções para número https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py 

'''

# Funções que estão na documentação para validação de dados tipo número: isnumeric(), isdigit() e isdecimal()

'''
Ao desenharmo por exemplo uma calculadora e por um acaso o usuário ao invés de digitar um número, digitar uma string
seja ela qual for, dará erro na execução do código e não conseguiremos prosseguir com a execução.
Uma das formas para impedir que isso aconteça é realizar uma validação com as funções mencionadas acima
elas realizam uma validação para ver se o caracter digitado pelo usuário ou indicado no código pode ser convertido
ou é um número, sendo assim em casos onde o usuarío digitar uma string ele validará antes de dar erro na execução do
código.
No exemplo abaixo iremos criar uma calculadora para realizar essa validação.
'''

#num_1 = input('Digite o primeiro número: ')
#num_2 = input('Digite o segundo número: ')

#if num_1.isdigit() and num_2.isdigit():
#    num_1 = int(num_1)
#    num_2 = int(num_2)
#
#    print()
#    print(f'O resultado da soma é: {num_1+num_2}')
#else:
#    print('Você precisa digitar um número!')

num_1 = input('Digite o primeiro número: ')
num_2 = input('Digite o segundo número: ')

if num_1.isdecimal() and num_2.isdecimal():
    num_1 = int(num_1)
    num_2 = int(num_2)

    print()
    print(f'O resultado da soma é: {num_1+num_2}')
else:
    print('Você precisa digitar um número!')


