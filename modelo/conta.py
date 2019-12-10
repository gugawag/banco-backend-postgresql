class Conta:

    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def debitar(self, valor):
        self.saldo -= valor

    def creditar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta_destino):
        self.debitar(valor)
        conta_destino.creditar(valor)

    def to_json(self):
        return self.__dict__