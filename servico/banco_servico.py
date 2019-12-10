from dao import banco_dao


class BancoServico:

    def debitar(self, valor, numero):
        conta_a_debitar = self.pesquisar_conta(numero)
        conta_a_debitar.debitar(valor)
        banco_dao.atualizar_saldo(conta_a_debitar)

    def creditar(self, valor, numero):
        conta_a_creditar = self.pesquisar_conta(numero)
        conta_a_creditar.creditar(valor)
        banco_dao.atualizar_saldo(conta_a_creditar)

    def transferir(self, valor, numero_origem, numero_destino):
        conta_origem = self.pesquisar_conta(numero_origem)
        conta_destino = self.pesquisar_conta(numero_destino)
        conta_origem.transferir(valor, conta_destino)

    def pesquisar_contas(self):
        contas = banco_dao.get_contas()
        return contas

    def pesquisar_conta(self, numero):
        conta = banco_dao.get_conta(numero)
        return conta

    def inserir_conta(self, conta_a_inserir):
        banco_dao.inserir_conta(conta_a_inserir)

    def remover_conta(self, numero):
        banco_dao.remover_conta(numero)
