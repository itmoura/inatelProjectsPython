from models.pessoa import Pessoa

class BancoDados:
    def __init__(self, nomeBanco, quantidadeTabelas):
        self.__nomeBanco = nomeBanco
        self.__quantidadeTabelas = quantidadeTabelas

        self.__registro = []

    def get_nomeBanco(self):
        return self.__nomeBanco

    def adiciona_registro(self, registro):
        self.__registro.append(registro)

    def mostra_registro(self):
        cont = 0

        for r in self.__registro:
            if isinstance(r, Pessoa):
                cont += 1

        print("Total Pessoas: ", cont)
