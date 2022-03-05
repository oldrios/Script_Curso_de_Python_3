'''
Dictionary Comprehension em Python
'''

'''
lista = [
    ('Key1', 'Value1'),
    ('Key2', 'Value2'),
    ('Key3', 'Value3'),
]

# lista = dict(lista) # Metodo 1 - Transformando em dicionário com dict() (mais fácil)
lista = {x: v for x, v in lista}  # Metodo 2 - Tansformando em dicionario com dict comprehensions
'''

d1 = {f'Chave_{x}': v for x, v in enumerate(range(5)) }  # Criando dicionário com dict comprehensions
d2 = {f'Key_{x}': x**2 for x in range(1024) if x % 4 == 0}  # Método mais usual

d2 = {x**2 for x in range(100)}  # Criando set comprehensions


print(d2)