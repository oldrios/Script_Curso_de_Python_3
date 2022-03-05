'''
Polimorfismo de sobreposição é o princípio que permite que classes derivadas de uma mesma
superclasse tenha métodos iguais (de mesma assinatura) mas compartamentos
diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros

Dois principais tipos de polimorfismo:

Polimorfismo de Sobreposição -> Mesma assinatura / Aplicado a classes diferentes
Polimorfismo de Sobrecarga -> Assinaturas diferentes / Aplicado a mesma classe
'''

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


c = C()
b = B()

c.fala('Oi')
b.fala('Oi')
