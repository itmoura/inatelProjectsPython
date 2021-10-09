from pymongo import MongoClient

def createCollection():
    return connect().create_collection("financeiro")

def connect():
    client = MongoClient('mongodb://localhost:27017')
    return client['concessionaria']

def _insert():
    connect().financeiro.insert_many([
        {
            "motor":1.8,
            "preco":25000
        },
        {
            "motor":250,
            "preco":7000
        },
        {
            "motor":1550,
            "preco":485000
        }
    ])

if __name__ == "__main__":
    # executar apenas na primeira vez se não tiver criado a collection na mão
    createCollection()
    # Inserir apenas uma vez, não foi criado validação
    _insert()
    financeiro = connect().financeiro
    veiculo = connect().veiculos

    ag1 = {
        "$lookup": {
            "from": "financeiro",
            "localField": "motor",
            "foreignField": "motor",
            "as": "Financeiro"
        }
    }

    ag2 = {
        "$project": {
            "_id": 0,
            "Modelo": "$modelo",
            "Ano": "$ano",
            "Preco": {
                "$arrayElemAt": ["$Financeiro", 0]
            }
        }
    }

    ag3 = {
        "$project": {
            "_id": 0,
            "Modelo": "$Modelo",
            "Ano": "$Ano",
            "Preco": "$Preco.preco"
        }
    }

    results = veiculo.aggregate([ag1, ag2, ag3])

    for aux in results:
        print('Modelo: ', aux["Modelo"])
        print('Ano: ', aux["Ano"])
        print('Preço: ', aux["Preco"])
        print("----------------------------")