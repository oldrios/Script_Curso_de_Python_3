'''
Operadores Relacionais
== Igual a
> Maior que
>= Maior que ou igual a
< Menor que
<= Menor que ou igual a
!= É diferente
'''

print('Essa é a tela de emprestimo, precisamos de algumas informações antes de começar.')
nome = input('Primeiro me diga, qual o seu nome? ')
idade = int(input(f'Certo {nome}, agora informe a sua idade: '))
#idade_minima = 18  # Idade mínima para solicitar o empréstimo.
idade_minima = 20
idade_maxima = 35

#print()
#if idade >= idade_minima:
#    print(f'{nome} você está apto para solicitar o empréstimo pois tem {idade} anos e já é maior de idade!')
#else:
#    print(f'{nome} você não pode solicitar o empréstimo pois tem {idade} anos, precisará de um responsável!')
#    print(f'Ou você pode aguardar {idade_minima - idade} ano(s) para solicitar.')

print()
if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} você está apto para solicitar o empréstimo pois tem {idade} anos e atende aos requisitos.')
elif idade < idade_minima:
    print(f'{nome} no momento você não atende aos requisitos para o empréstimo,')
    print('Você pode solicitar a uma pessoa entre 20 e 30 anos para solicitar o empréstimo.')
    print(f'Ou você pode esperar {idade_minima - idade} ano(s) para solicitar seu empréstimo!')
elif idade > idade_maxima:
    print(f'{nome} no momento você não atende aos requisitos para o empréstimo,')
    print(f'Infelizmente você já tem {idade - idade_maxima} ano(s) a mais do que o requisito necessário.')
else:
    print(f'{nome} você tem certeza que digitou a idade certa?')
    print(f'Aqui está dizendo que sua idade é {idade}, parece que temos um erro.')
