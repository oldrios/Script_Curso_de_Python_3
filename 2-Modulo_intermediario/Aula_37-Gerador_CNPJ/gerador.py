from time import sleep
from random import randint


def header():
    print('*=' * 30)
    print('                 GERADOR DE CNPJ 1.0.0')
    print('*=' * 30, '\n')


def gerador_indice(cnpj):
    if len(cnpj) == 12:
        n = 5
    elif len(cnpj) == 13:
        n = 6

    i1 = (x for x in range(n, 1, -1))
    i2 = (x for x in range(9, 1, -1))
    indice = list(i1) + list(i2)
    return indice


def gerador_de_digito(cnpj_temp):
    indice = gerador_indice(cnpj_temp)
    total = (int(n) * indice[i] for i, n in enumerate(cnpj_temp))
    validacao = 11 - (sum(total) % 11)
    digito1 = validacao if validacao < 10 else 0  # Gerando o primeiro digito do CNPJ
    cnpj_temp += str(digito1)

    indice = gerador_indice(cnpj_temp)
    total = (int(n) * indice[i] for i, n in enumerate(cnpj_temp))
    validacao = 11 - (sum(total) % 11)
    digito2 = validacao if validacao < 10 else 0   # Gerando o segundo digito do CNPJ
    cnpj_temp += str(digito2)

    return cnpj_temp


def gerador_cnpj():
    cnpj = ''
    for i in range(8):
        cnpj += str(randint(1, 9))
    cnpj += '0001'
    cnpj = gerador_de_digito(cnpj)
    return cnpj

def progress(n):
    for v in range(n):
        print('||' * (v + 1), end='')
        sleep(0.2)

def executor():
    header()
    opcao = input('Deseja gerar um novo CNPJ válido? (s)im ou (n)ão: ')
    while opcao.lower() == 's' or opcao.lower() == 'sim':
        print(f'O CNPJ gerado com sucesso: {gerador_cnpj()}')
        opcao = input('Deseja gerar um novo CNPJ válido? (s)im ou (n)ão: ')
    print('Saindo... Xau xau!')
    progress(7)

if __name__ == '__main__':
    executor()








