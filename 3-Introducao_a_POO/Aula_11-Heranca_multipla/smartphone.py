from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} está desligado, ligue o dispositivo.'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado.'
            print(error)
            self.log_error(error)
            return

        self._conectado = True
        info = f'{self._nome} agora está conectado.'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._ligado:
            error = f'{self._nome} está desligado, ligue o dispositivo.'
            print(error)
            self.log_error(error)
            return

        if not self._conectado:
            error = f'{self._nome} não está conectado!'
            print(error)
            self.log_error(error)
            return

        self._conectado = False
        info = f'{self._nome} agora está desconectado.'
        print(info)
        self.log_info(info)

    def desligar(self):
        if not self._ligado:
            return

        else:
            self._ligado = False
            if self._conectado:
                self._conectado = False

