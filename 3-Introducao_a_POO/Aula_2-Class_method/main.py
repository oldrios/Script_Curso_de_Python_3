from random import randint

class Pessoa():
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        return randint(10000, 19999)


person1 = Pessoa('James', 26)
person2 = Pessoa.por_ano_de_nascimento('Ben', 1996)

print(person1.nome, person1.idade, person1)
print(person2.nome, person2.idade, person2)
print(Pessoa.gera_id())
print(person1.gera_id())







