'''
public, protected and private

Nas linguagens tradicionais temos o seguinte modo para indicar quando um
atributo de uma classe pode ou não ser acessado(alterado). Quando o atributo
é "públic" (pode ser acessado fora da classe), quando é "protected"
(recomenda-se não acessar fora da classe) ou quando é "private"
(a linguagem de programação "proíbe" que se acesse o atributo fora
da classe).

Já em Python essa atitude de "bloquear um comando" vai contra a sua própria
filosofia, então a linguagem foi desenvolvida para não ter essa "trava". Então
por convenção dos próprios programadores de Python para indicarmos quando um
atributo pode ou não ser acessado fora da classe indicamos da seguinte forma:

class A:
    atributo = 'Public' - Pode ser acessado fora da classe
    _atributo = 'Protected' - '1 _'Não pode ser acessado fora da classe (recomendação do programador)
    __atributo = 'Private' - '2 __'Fica intrínseco que não se pode acessar fora da classe
'''


class BancoDeDados:
    def __init__(self):
#        self.dados = {}  # Public: Pode ser acessado fora da classe
#        self._dados = {}  # "Private leve": Não se deve acessar fora da classe
        self.__dados = {}  # "Private pesado": indicação intrínseca que não se deve acessar fora da classe

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, cliente in self.__dados['clientes'].items():
            print(id, cliente)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BancoDeDados()

bd.inserir_clientes(1, 'Ana')
bd.inserir_clientes(2, 'Maria')
bd.__dados = 'asds'
print(bd.__dados)
bd.inserir_clientes(3, 'Helena')
bd.apagar_cliente(2)
bd.listar_clientes()















