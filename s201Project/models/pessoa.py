from models.registro import Registro

class Pessoa(Registro):
	def __init__(self, nome, idade):
		super().__init__(nome, idade)

	def get_nome(self):
		return self.__nome

	def get_idade(self):
		return self.__idade