from models.bancoDados import BancoDados
from models.pessoa import Pessoa
from models.animal import Animal

if __name__ == "__main__":
	p1 = Pessoa("Luiza", 20, 1, "06/07")
	p2 = Pessoa("Ítalo", 22, 2, "06/07")

	a1 = Animal("lola", 3, 3, "06/07")
	b = BancoDados("S201 Prova", 4, p1)

	b.adiciona_registro(p2)
	b.adiciona_registro(a1)

	b.mostra_registro()

