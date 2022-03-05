class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = []

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def endereco(self):
        return self.__endereco

    def insere_endereco(self, cidade, estado):
        self.__endereco.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for x in self.endereco:
            print(f'Cidade: {x.cidade} / UF: {x.estado}')

    def __del__(self):
        print(f'\n{self.nome} foi apagado!')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado!')