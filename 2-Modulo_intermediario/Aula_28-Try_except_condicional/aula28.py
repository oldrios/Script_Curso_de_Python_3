'''
Usando Try e Except como condicional em Python
'''
from random import randint

def convert_num(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    num = convert_num(input('Digite o num a ser multiplicado: '))
    num2 = randint(1, 10)
    if num is not None:
        print(f'A multiplicação foi realizada, você digitou {num} e escolhemos {num2}')
        print(f'{num * num2} é o seu resultado!\n')
        print('_=' * 30)
    else:
        print(f'Iiih, erro! Precisa digitar um número. ¬¬ "{num}"\n')
        print('_=' * 30)

