from re import sub
from time import sleep


def header():
    print('*=' * 30)
    print('                 VALIDADOR DE CNPJ 1.0.0')
    print('*=' * 30, '\n')


def remove_pontos(cnpj):
    return sub(r'[^0-9]', '', cnpj)


def gerador_indice(cnpj):
    if len(cnpj) == 12:
        n = 5
    elif len(cnpj) == 13:
        n = 6

    i1 = (x for x in range(n, 1, -1))
    i2 = (x for x in range(9, 1, -1))
    indice = list(i1) + list(i2)
    return indice


def validador(cnpj):
    cnpj_temp = cnpj[:-2]

    indice = gerador_indice(cnpj_temp)
    total = (int(n) * indice[i] for i, n in enumerate(cnpj_temp))
    validacao = 11 - (sum(total) % 11)
    digito1 = validacao if validacao < 10 else 0  # Validando o primeiro digito do CNPJ
    cnpj_temp += str(digito1)

    indice = gerador_indice(cnpj_temp)
    total = (int(n) * indice[i] for i, n in enumerate(cnpj_temp))
    validacao = 11 - (sum(total) % 11)
    digito2 = validacao if validacao < 10 else 0   # Validando o segundo digito do CNPJ
    cnpj_temp += str(digito2)

    return cnpj_temp == cnpj


def progress(n):
    for v in range(n):
        print('||' * (v + 1), end='')
        sleep(0.2)


def executor():
    opcao = 's'
    while opcao.lower() == 's' or opcao.lower() == 'sim':
        header()
        try:
            cnpj = input('Digite o CNPJ: ')
            cnpj = remove_pontos(cnpj)
            if validador(cnpj):
                print(f'O CNPJ é válido!')
            else:
                print(f'Erro! O CNPJ informado não é válido!')
        except TypeError:
            print('Você precisa digitar um CNPJ completo (com ou sem pontuação).\n'
                  'OBS: Não utilizar letras!')
        except UnboundLocalError as erro:
            print('Você precisa digitar um CNPJ completo (com ou sem pontuação)\n'
                  'OBS: Não utilizar letras!')
        opcao = input('Deseja realizar outra validação? (s)im ou (n)ão: ')
    print('Saindo... Xau xau!')
    progress(7)


if __name__ == '__main__':
    executor()
