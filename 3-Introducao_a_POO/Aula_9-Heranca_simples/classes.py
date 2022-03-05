class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_da_classe} está falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_da_classe} está comprando')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_da_classe} está estudando')
