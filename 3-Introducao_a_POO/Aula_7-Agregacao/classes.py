from re import sub


class Carrinho:
    def __init__(self):
        self.carrinho = []

    def inserir_produtos(self, produto):
        self.carrinho.append(produto)

    def lista_produtos(self):
        for produto in self.carrinho:
            print(produto.nome, produto.preco)

    def soma_total(self):
        total = sum((x.preco for x in self.carrinho))
        print(total)


class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco (self, setvalor):
        self._preco = sub(r'[^0-9]', '', setvalor)