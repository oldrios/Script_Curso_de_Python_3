'''
Contadores + acumuladores com While e Else
'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    if contador > 6:
        break

    acumulador += contador
    contador += 1
else:
    print('Acabou a contagem')
print('Você finalizou o codigo com break')


