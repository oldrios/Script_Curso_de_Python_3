'''
Funções DEF em Python
'''

'''
def funcao(a=0, b=0, c=0, d=0, e=0):
    soma = a + b + c + d + e
    return f'O resultado da sua soma é: {int(soma)}'


a = 456 * 2
b = 20 + 10
c = 82 - 54
d = 2 / 2
e = 8 ** 2

print(a)
print(b)
print(c)
print(d)
print(e)

print(funcao(a, b, c, d, e))
'''

'''
def titulo(text):
    print('-' * len(text))
    print(text)
    print('-' * len(text))


titulo('O rato roeu a roupa do rei de roma')
'''

'''
# Desafio: Faça um programa com a função chamada área() e calcule a área do terreno

def área(a, b):
    a = float(a)
    b = float(b)
    area = a * b
    return f'A área do seu terreno é {area:.2f}m²'

def header(txt):
    print('-=' * (int(len(txt) / 2)))
    print(txt)
    print('-=' * (int(len(txt) / 2)))


opcao = 'S'

while opcao.lower() == 's' or opcao.lower() == 'sim':

    header('    DESMEMBRAMENTO E REPARTIÇÃO DE TERRENOS - SP    ')

    largura = input('Digite a largura do terreno (em metros): ')
    comprimento = input('Digite o comprimento do terreno (em metros): ')

    print(área(largura, comprimento))
    opcao = input('Deseja calcular outra área? [s]im ou [n]ão: ')
    
'''

'''
Desafio fazer um contador que conte de 1 a 10 de 1 em 1, conte de 10 a 0 de 2 em 2 
e por ultimo uma personalizada pelo usuário 
'''

'''
def contador(inicio=0, fim=0, passo=1):
    lista_contador = []
    repeticoes = []
    if passo < 0:
        passo *= -1

    if inicio < fim:
        for valor in range(0, int((fim - inicio)/passo+1)):
            repeticoes.append(valor)
        for n in repeticoes:
            cont = 0
            cont = passo * n + inicio
            lista_contador.append(int(cont))
    elif inicio > fim:
        for valor in range(0, int((inicio-fim)/passo+1)):
            repeticoes.append(valor)
        for n in repeticoes:
            cont = 0
            cont = (passo * -n) + inicio
            lista_contador.append(int(cont))
    else:
        print(f'Operação inválida para o contador, os parâmetros devem ser (Inicio, Fim, Passo).')
        print(f'Lembrando que Inicío e Fim não podem ser iguais e o passo não pode ser zero.')
    print(f'Sua contagem é {lista_contador}')


contador(100, 15, 5)
'''
from time import sleep

# Melhorando código do desafio acima

def contador(inicio=0, fim=0, passo=1):
    print(f'Contando listagem de {inicio} a {fim} no intervalo de {passo}', flush=True)
    sleep(0.2)
    lista_contador = []
    c = inicio
    if passo < 0:
        passo *= -1

    if inicio < fim:
        while c < fim:
            lista_contador.append(c)
            c += passo

    elif inicio > fim:
        while c > fim:
            lista_contador.append(c)
            c -= passo

    else:
        print(f'Operação inválida para o contador, os parâmetros devem ser (Inicio, Fim, Passo).')
        print(f'Lembrando que Inicío e Fim não podem ser iguais e o passo não pode ser zero.')

    for n in lista_contador:
        print(f'{n}', end=' ')
        sleep(0.2)
    print()
    print('_' * 2 * len(lista_contador))


contador(1, 10, 1)
contador(20, 1, 2)

print('Sua vez de inserir uma contagem!')
i = int(input('NUM INICIAL:  '))
f = int(input('NUM FINAL:    '))
p = int(input('PASSO:        '))
contador(i, f, p)




