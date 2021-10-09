from Conta import Conta

class Depositar(Conta):
    def __init__(self, deposito):
        super().__init__(self)
        if deposito < 0:
            raise ValueError("Não é possivel depositar valor negativo!!")
        else:
            self.saldo = deposito