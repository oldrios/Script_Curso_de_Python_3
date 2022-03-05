'''
Levantando as exceções em Python
'''

# https://docs.python.org/3/library/exceptions.html

def divide(n1, n2):
    if n1 == 0 or n2 == 0:
        raise ValueError('Não há divisão para o número 0')  # Dessa forma, aparecerá essa msg ao  dar erro
    return n1 / n2

print(divide(5, 0))

