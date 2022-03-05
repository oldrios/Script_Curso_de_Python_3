'''
Herança múltipla
'''

'''
class A:
    def falar(self):
        print('Falando... Estou em A')


class B(A):
    def falar(self):
        print('Falando... Estou em B')


class C(A):
    def falar(self):
        print('Falando... Estou em C')


class D(C, B):  # A ordem das classes inputadas no parâmetro da cls D tem ordem de verificação da esquerda para direita
    pass


d = D()
d.falar()
'''

from smartphone import *


device = Smartphone('Motorola V3')

device.conectar()
device.desconectar()
device.ligar()
device.conectar()
device.conectar()
device.desligar()
device.conectar()
device.ligar()
device.desconectar()
device.conectar()



