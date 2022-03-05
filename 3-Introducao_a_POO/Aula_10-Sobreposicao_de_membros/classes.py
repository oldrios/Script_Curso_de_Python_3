class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_da_classe} está falando')

    def outra_fala(self):
        print(f'Estou na hierarquia Pessoa')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_da_classe} dss está comprando')

    def outra_fala(self):
        print(f'Estou na hierarquia Cliente')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, classfication):
        super().__init__(nome, idade)
        self.classification = classfication

    def outra_fala(self):
        print(f'Estou na hierarquia ClienteVIP')  # Hierarquia dessa mesma classe
        super().outra_fala()  # Acessando hierarquia 'acima', nesse caso Cliente
        Pessoa.outra_fala(self)  # Acesssando a hierarquia Pai, nesse caso Pessoa




class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_da_classe} está estudando')
