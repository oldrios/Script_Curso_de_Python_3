'''
Condições IF, ELIF e ELSE
'''

if False:
    print('Essa condição é verdadeira')
    print()
    print('Vamos calcular então')
    num_1 = int(input('Digite um número: '))
    num_2 = int(input('Digite outro número: '))
    print('Faremos uma adição, ok?')
    print(f'O resultado da soma é: {num_1 + num_2}')
elif False:
    print('Essa condição tabém é verdadeira')
    print()
    surprise = input('Digite algo para complementar o comando: ')
    print(f'Você digitou algo que foi acrescentado a variável surprise = {surprise}')
elif True:
    print('Já essa é falsa, mas talves possa mudar.')
else:
    print('Nenhuma das condições acima foram verdadeiras, logo, eu começo a valer.')

