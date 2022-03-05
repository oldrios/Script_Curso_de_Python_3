# Desafio 1 - Número inteiro

print('Bem vindo ao software!')
print()
num = input('Digite um número inteiro: ')


if num.isdigit():
    num = int(num)
    if (num % 2 == 0):
        print(f'O número digitado foi {num} e ele é um número par, obrigado!')
    else:
        print(f'O número digitado foi {num} e ele é um número ímpar, obrigado!')
else:
    print(f'Como solicitado, preciso de um número inteiro e você digitou {num}')
    print('Tente novamente')


'''
# Desafio 2 - Saudação!

print('Bem vindo ao software!')
print()
hora = input('Por favor, me informe que horas são? (digite apenas o número correspondente à hora): ')

if hora.isdecimal():
    hora = int(hora)
    if (hora >= 0 and hora <= 11) or hora == 24:
        if hora != 24:
            print(f'Bom dia, é {hora}am!')
        else:
            print('Bom dia, é 0am!')
    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde! Já são {hora}pm, suas atividades já foram concluidas? Ainda tenho pendencias, vou indo!')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite! Agora são {hora}pm, você já está com sono? Pois eu estou, tchaaau!')
    else:
        print('Você sabe que o dia vai de 0 hora até 23 horas, certo?')
        print(f'Não existe {hora} horas, tente digitar outra hora.')
else:
    print(f'Você precisa digitar um número e não é permitido digitar {hora}.')
    print('Rode o código e tente novamente')
'''


# Desafio 3 - Contando letras do nome

print('Bem vindo ao software!')
print('Iremos analisar seu nome')
print()

nome = input('Digite seu primeiro nome: ')
qtd_char = len(nome)

if qtd_char <= 4 and qtd_char >= 1:
    print(f'Seu nome é curto tem apenas {qtd_char} letra(s).')
elif qtd_char >= 5 and qtd_char <= 6:
    print(f'Seu nome é normal, geralmente nomes tem entre 5 e 6 letras e o seu tem {qtd_char} letras.')
elif qtd_char > 6:
    print(f'Seu nome é grande, tem {qtd_char} letras, maior que a média.')
else:
    print('Por que você não digitou nada? Coloque seu nome, será legal!')


