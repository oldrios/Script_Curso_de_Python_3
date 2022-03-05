'''
Operador ternário em Python
'''

'''
# Operação normal

logged_user = False

if logged_user:  # Omitindo a expressão lógica, automaticamente declaramos que a variável é igual a True
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa fazer o login!'

print(msg)

# Exemplo de operação ternária

logged_user = False
msg = 'Usuário logado.' if logged_user else 'usuario precisa fazer login.'

print(msg)
'''
idade = 18
while True:

    idade_user = input('Digite sua idade: ')



    if idade_user.isdigit():
        idade_user = int(idade_user)
        msg = 'Bem vindo ao software!' if idade_user >= idade else 'Você não tem permissão para entrar!'
    else:
        print('Você precisa digitar sua idade!')
        continue

    print(msg)
    break


