import sys

list_size = [1, 2, 3, 4, 5, 6, 7, 'OMG', 'Yeaaaaah', 'How to make']
tuple_size = (1, 2, 3, 4, 5, 6, 7, 'OMG', 'Yeaaaaah', 'How to make')
cont_l = 1
cont_t = (1,)

for n in range(100):
    list_size.append(cont_l)
    tuple_size += cont_t


print(f'Tamanho da lista = {sys.getsizeof(list_size)}')
print(f'Tamanho da tupla = {sys.getsizeof(tuple_size)}')
print(f'Diferença entre a lista e tupla: {(sys.getsizeof(list_size) / sys.getsizeof(tuple_size) - 1) * 100:.2f}%'
      f' a mais de espaço ocupado pela lista')
