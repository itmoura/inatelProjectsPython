class Registro:
    def __init__(self, id, dataCriacao):
        self.__id = id
        self.__dataCriacao = dataCriacao

    def get_id(self):
        return self.__id

    def get_dataCriacao(self):
        return self.__dataCriacao

