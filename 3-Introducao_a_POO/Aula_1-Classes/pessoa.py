class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não vai falar de boca cheiaaaaa! Mas que falta de educação ein.')
            return
        if self.comendo:
            print(f'Tu quer entupir o {self.nome}? Esse marginal já tá comendo!')
            return

        print(f'{self.nome} está comendo {alimento}, nem dividiu esse vacilão.')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está nem comendo mané.')
            return

        print(f'{self.nome} parou de comer, também depois de engordar 10kg só agora.')
        self.comendo = False

    def falar(self, assunto, com_quem):
        if self.comendo:
            print(f'{self.nome} está comendo meu parsa, não fala de boca cheia!')
            return
        if self.falando:
            print(f'Esse tagarela do {self.nome} náo fecha a matraca, tu quer que ele fale mais oque? Não dá.')
            return

        print(f'Olha só, {self.nome} tá trocando um papo sobre {assunto} com {com_quem}.')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'Tá mandando quem calar a boca? O {self.falando} tá na dele, sem falar nada.')
            return

        print(f'{self.nome} tá falando demais mesmo, fechou o bico agora e parou de falar.')
        self.falando = False

    def envelhecer(self, anos):
        self.idade += anos

    def doar_idade(self, anos, pessoa_destino):
        self.idade -= anos
        pessoa_destino.idade += anos
        print(f'Olha a mágica triim! Brother que pilantra {self.nome} ficou mais novo '
              f'{anos} anos\n e {pessoa_destino.nome} ficou mais velho xD, se lascou')

