'''
Operadores Lógicos
and, or, not
in e not in
'''

a = 1
b = 2

# Os operadores OR e AND utilizam a tabela verdade para validar uma expressão se é verdadeira ou não

# O operador lógico NOT quando utilizado inverte o IF para trazer resultados falsos ao invés de verdadeiro
# ou seja, sendo o IF uma cláusula para comparar uma exmpressão e trazer os dados da sua hierarquia como verdadeiros
# quando utilizando o NOT trará os comandos da hierarquia IF caso a expressão seja falsa

'''
if not a != b:
    print('Expressão é falsa, por isso retornou aqui.')
else:
    print('Expressão não é falsa, por isso apareceu aqui.')
'''

'''
nome = input('Digite seu nome e verificaremos se não tem a letra "i" nele: ')

if 'i' not in nome:
    print('Não tem a letra i no seu nome')
else:
    print('Tem a letra i no seu nome')
'''

usuario = input('Nome de usuario: ')
senha = input('Senha do usuario: ')
usuario_bd = 'Oldaque'
senha_bd = '1234'

if usuario_bd == usuario and senha_bd == senha:
    print(f'{usuario_bd} você está logado!')
else:
    print(f'Usuario: {usuario} e/ou senha não encontrados')
