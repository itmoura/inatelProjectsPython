class Conta:
    def __init__(self):
        self.saldo = 0

    def depositar(self, deposito):
        super().__init__(self)
        if deposito < 0:
            raise ValueError("Não é possivel depositar valor negativo!!")
        else:
            self.saldo = deposito

    def consultarSaldo(self):
        print("Seu saldo é: ", self.saldo)