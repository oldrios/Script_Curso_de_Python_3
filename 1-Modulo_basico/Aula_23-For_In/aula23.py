'''
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
'''

'''
string = 'Realizando loop com for in'


for n, letra in enumerate(string):
    print(n, letra)

'''
'''
for n in range(0,100,1):
    print(n)
'''

'''
# Decrementando

for n in range(100,0,-1):
    print(n)
'''

'''
# Achando múltiplos

for n in range(0,257,8):  # Intervalo contará de 8 em 8
    print(n)



for n in range (257):
    if n % 8 == 0:
        print (n)
'''

texto = 'Python'
novo_texto = ''

for letra in texto:
    if letra == 't':
        novo_texto += letra.upper()
    elif letra == 'h':
        break
        novo_texto += letra.upper()
    else:
        novo_texto += letra


print(novo_texto)