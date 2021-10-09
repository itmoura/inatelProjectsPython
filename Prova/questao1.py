def myOrder(film):
    return film['ano']

filmes = []
filmAno = set()

while(int(input("Cadastrar filme? (1 -> sim, 2 -> Não): ")) == 1):
    nome = input("Digite nome do Filme: ")
    ano = input("Digite ano do filme: ")
    filme = {
        'nome': nome,
        'ano': ano
    }
    filmAno.add(ano)
    filmes.append(filme)
print("  ")
print("a. Quantos filmes foram cadastrados;")
print("Foram cadastrados ", len(filmes), " filmes")
print("------------------------------------")

print("b. Um conjunto com os diferentes anos cadastrados; ")
print(filmAno)
print("------------------------------------")

print("c. As Informações do(s) filme(s) do ano mais recente;")
filmes.sort(key=myOrder, reverse=True)
anoF = filmes[0]['ano']
for filme in filmes:
    if(anoF == filme['ano']):
        print("Nome do filme: ", filme['nome'], " ano do filme", filme['ano'])
print("------------------------------------")
