'''
Iterando strings com While
'''

print('Seja bem vindo ao contador de letras')
opcao = input('Deseja começar a contagem? [s]im ou [n]ão: ')

while opcao == 's':
    minha_string = input('Digite uma frase e começarei a contagem: ')
    qtd_char_string = len(minha_string)

    c = 0
    contagem_atual = 0
    letra = ''

    while c < qtd_char_string:
        qtd_vezes_letra = minha_string.count(minha_string[c])

        if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra

        c += 1

    print(f'A letra "{letra}" aparece {contagem_atual} vezes, portanto a letra que mais se repete')
    print()
    opcao = input('Deseja fazer outra contagem? [s]im ou [n]ão: ')
print()
print('Obrigado, programa será finalizado!')



'''
# Colocando as letras R em maiúsculo

if minha_string[c] == 'r':
    nova_string += minha_string[c].upper()
else:
    nova_string += minha_string[c]

'''