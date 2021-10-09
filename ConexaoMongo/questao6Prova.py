from pymongo import MongoClient

def connect():
    client = MongoClient('mongodb://localhost:27017')
    return client['educacao']

if __name__ == "__main__":
    escola = connect().escola
    professor = connect().professor

    ag1 = {
        "$lookup": {
            "from": "escola",
            "localField": "cpf",
            "foreignField": "cpf_prof",
            "as": "Escola"
        }
    }

    ag2 = {
        "$project": {
            "_id": 0,
            "Nome": "$nome",
            "CidadeNatal": "$natural.cidade",
            "AnoNasc": "$ano_nasc",
            "Escola": {
                "$arrayElemAt": ["$Escola", 0]
            }
        }
    }

    ag3 = {
        "$project": {
            "_id": 0,
            "Nome": "$Nome",
            "CidadeNatal": "$CidadeNatal",
            "AnoNasc": "$AnoNasc",
            "Escola": "$Escola.nome"
        }
    }

    results = professor.aggregate([ag1, ag2, ag3])

    for aux in results:
        print('Nome: ', aux["Nome"])
        print('Cidade Natal: ', aux["CidadeNatal"])
        print('Ano de Nascimento: ', aux["AnoNasc"])
        print('Escola: ', aux["Escola"])
        print("----------------------------")