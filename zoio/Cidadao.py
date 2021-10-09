from Pessoa import Pessoa


class Cidadao(Pessoa):
    def __init__(self, nome, sexo, idade, cpf):
        super().__init__(nome, sexo, idade)
        self.cpf = cpf

    def apresentar(self):
        super().apresentar()
        print("CPF: ", self.cpf)