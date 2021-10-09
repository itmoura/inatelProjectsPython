class Pessoa:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo

        if idade < 0:
            raise ValueError("Valor de idade inválido!!")
        else:
            self.idade = idade

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print("Sexo: ", self.sexo)
        print("Idade: ", self.idade)