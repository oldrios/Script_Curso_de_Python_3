print('Bem vindo ao validador de CPF')

cpf_user = input('Digite o CPF a ser validado: ')
cpf_lista = []
cpf_validador = []
digito_1 = 0
digito_2 = 0
cont = 0

# Transformando strings digitadas em lista

for n in cpf_user:
    cpf_lista.append(int(n)) if n.isdigit() else ...
    continue

# Validando digito 1 do CPF

for c in range(10,1,-1):
    cpf_validador.append(cpf_lista[cont] * c)
    cont += 1

if (11 - (sum(cpf_validador) % 11)) > 9:
    digito_1 = 0
else:
    digito_1 = (11 - (sum(cpf_validador) % 11))


# Validando digito 2 do CPF

cpf_validador = []
cont = 0

for c in range(11,2,-1):
    cpf_validador.append(cpf_lista[cont] * c)
    cont += 1

cpf_validador.append(digito_1 * 2)

if (11 - (sum(cpf_validador) % 11)) > 9:
    digito_2 = 0
else:
    digito_2 = (11 - (sum(cpf_validador) % 11))

# Criando CPF temporário para validação

cpf_validador = []
cont = 0

for c in range(0,9,1):
    cpf_validador.append(cpf_lista[cont])
    cont += 1

cpf_validador.append(digito_1)
cpf_validador.append(digito_2)


print('CPF Digitado é valido!!') if cpf_lista == cpf_validador else print('CPF Digitado é invalido!')



