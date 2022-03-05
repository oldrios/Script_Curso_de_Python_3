'''
While em python
Utilizando para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
'''

'''
x = 0

while x <= 12:
    print(x)
    x = x + 1
else:
    print('Cabooou!')
'''
'''
x = 'ab'
y = 'abaaaaaaaa'

while x != y:
    print(x)
    x = x + 'a'
else:
    print('Caboou')
'''

'''

# Utilizando o break e continue

x = 0

while x <= 12:
    if x == 6:
        print('Meia duzia')
        x += 1
        continue
        #  break

    print(x)
    x += 1
else:
    print('Acabou!')

'''

'''
# Criando um laço, dentro de outro laço

x = 0  # Coluna

while x < 5:

    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1

print('Acabou o código!')
'''

# Criando uma "calculadora"

opcao = input('Vamos fazer contas, deseja continuar? [s]im ou [n]ão: ')

while opcao == 's':
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operacao = input('Coloque o simbolo da operação desejada: ')

    if not num_1.isdigit() or not num_2.isdigit():
        print('Você não digitou um número!')
        opcao = input('Deseja fazer outra conta? [s]im ou [n]ão: ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operacao == '+':
        print(num_1 + num_2)
    elif operacao == '-':
        print(num_1 - num_2)
    elif operacao == '*':
        print(num_1 * num_2)
    elif operacao == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido!')

    opcao = input('Deseja fazer outra conta? [s]im ou [n]ão: ')

else:
    print()
    print('Saindo do programa...')

