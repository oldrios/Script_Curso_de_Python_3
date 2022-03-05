'''
Try - Tente
Except - Exceto
'''


try:
    nao_tem_essa_variavel = {}
    print(nao_tem_essa_variavel[2])
except NameError as erro:
    print('O seu erro é que:', erro)
except (IndexError, KeyError) as idx:
    print('Pois é rapaz, olha ai erro de indice/chave:', idx)
except Exception as exc:
    print('Aconteceu um erro inesperado.', exc)

print('O código não para!')


