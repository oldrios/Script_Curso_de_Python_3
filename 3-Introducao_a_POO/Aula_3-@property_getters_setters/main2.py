class Pessoa:

    def __init__(self, nome, cpf, altura):
        self.nome = nome
        self._cpf = cpf
        self.altura = altura

    @property
    def _cpf(self):
        return self.ocpf

    @_cpf.setter
    def _cpf(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('.','')
            valor = int(valor.replace('-',''))

        self.ocpf = valor
        return valor


jovem1 = Pessoa('Jovanilson', '954.321.645-65', '2,62')

print(jovem1.nome, jovem1.altura, jovem1._cpf)


