from models.registro import Registro

class Animal(Registro):
	def __init__(self, apelido, idade):
		super().__init__(apelido, idade)
