'''
1 - Criar uma função que exiba uma saudação com os parâmetros saudação e nome.
'''

'''
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
'''

'''
3 - Crie uma função que receba 2 números, o primeiro é um valor e o segundo um percentual (ex. 100%).
Retorne o valor do primeiro número somado do aumento do percentual do mesmo.
'''

'''
4 - Fizz e Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da função for divisível
por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado
'''

'''
# Resolução exercício 1

def saudacao(nome):
    return f'Olá {nome}'

var = saudacao('Oldaque')
print(var)
'''
'''
# Resolução exercício 2

def soma(a=0, b=0, c=0):
    return f'A soma dos parâmetros informado é: {a + b + c}'

var = soma(2, 4, 6)
print(var)
'''
'''
# Resolução exercício 3

def aumento(a, b):
    b = b / 100
    return f'O aumento de {b*100}% foi aplicado a {a}. Seu total com o aumento é {a+b*a}'

var = aumento(50, 10)

print(var)
'''

# Resolução exercício 4

def fbzz(a):
    if a % 5 == 0 and a % 3 == 0:
        return 'FizzBuzz'
    elif a % 3 == 0:
        return 'Fizz'
    elif a % 5 == 0:
        return 'Buzz'
    else:
        return a

var = fbzz(303)


print(var)


