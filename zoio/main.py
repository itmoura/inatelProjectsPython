from Cidadao import Cidadao
from Pessoa import Pessoa

nome = input("Nome da pessoa: ")
sexo = input("Sexo da pessoa: ")
idade = int(input("Idade da pessoa: "))
pessoa_1 = Pessoa(nome, sexo, idade)

pessoa_1.apresentar()


nome = input("Nome da pessoa: ")
sexo = input("Sexo da pessoa: ")
idade = int(input("Idade da pessoa: "))
cpf = input("Cpf da pessoa: ")
cidadao_1 = Cidadao(nome, sexo, idade, cpf)

cidadao_1.apresentar()
