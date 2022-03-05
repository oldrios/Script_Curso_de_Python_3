'''
Utilizando a função len() para contar a quantidade de caracteres em uma string
'''

'''
var_1 = input('Digite algo para alimentar a primeira variável: ')
var_2 = input('Digite outra coisa para alimentar a segunda variável: ')

print(f'Você digitou {len(var_1) + len(var_2)} caracteres.')
'''

# Verificar se a quantidade de caracter atende o requisito de 15 caracteres
print('Vamos começar com o desafio, dessa vez é fácil!')
print('Nesse desafio você só precisará digitar 15 carateres aleatórios, lembre-se, são exatamente 15 caracteres!')
print('Obs: Espaços também contam como um caracter em uma string. Essa dica é importante!')
print()

desafio_1 = input('Você entendeu as instruções? digite (S) para continuar ou (N) para parar: ')

if desafio_1 == 'S':
    print('Muito bem, então vamos comeaçar')
    var_1 = input('Digite a quantidade de caracteres solicitadas na segunda mensagem enviada: ')
    qtd_caracter = len(var_1)
    print()
    if qtd_caracter == 15:
        print(f'Muito bem! Você digitou exatamente {qtd_caracter} caracteres, você completou o desafio!')
    else:
        print(f'Que pena, você perdeu o desafio pois digitou {qtd_caracter} caractere(s), comece o código e tente novamente')
else:
    print(f'Você disse {desafio_1} e entendi que você não entendeu as instruções e '
          f'portanto optou por não continuar o desafio, rode o código novamente e')
    print('escolha iniciar o desafio após entender as intruções.')




