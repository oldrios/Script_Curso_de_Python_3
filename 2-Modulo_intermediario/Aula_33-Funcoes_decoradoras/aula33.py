'''
Funções decoradoras
'''

'''
def master(funcao):
    def slave():
        print('Hit the road jack')
        funcao()
    return slave


@master  # Decorador
def hlwd():
    print('Hello fucking world!')


# a = master(hlwd)  # método incomum (não utilizando decoradores)

a = hlwd()

a
'''
from time import sleep, time


# Medindo a velocidade de execução de uma função
def velocidade(funcao):
    def medidor(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        time_total = end_time - start_time
        print(f'O {funcao.__name__} foi iniciado, foi um total de {time_total:.9f}'
              f'seg para ser executado')
        return resultado
    return medidor()

# Decorando
@velocidade
def lazy_function():
    for n in range(100000):
        print(n, end='.')


a = lazy_function

a










