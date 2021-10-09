from pymongo import MongoClient

def connect():
    client = MongoClient('mongodb://localhost:27017')
    return client['GDH']

if __name__ == "__main__":
    pacientes = connect().pacientes
    leitos = connect().leitos

    ag1 = {
        "$lookup": {
            "from": "leitos",
            "localField": "leito",
            "foreignField": "numero",
            "as": "Leitos"
        }
    }

    ag2 = {
        "$project": {
            "_id": 0,
            "Nome": "$nome",
            "AnoNasc": "$ano_nasc",
            "Dor": "$enfermidade",
            "Leito": {
                "$arrayElemAt": ["$Leitos", 0]
            }
        }
    }

    ag3 = {
        "$project": {
            "_id": 0,
            "Nome": "$Nome",
            "AnoNasc": "$AnoNasc",
            "Dor": "$Dor",
            "Leito": "$Leito.numero",
            "Sala": "$Leito.sala",
            "Analgesico": "$Leito.medicamento.analgesico",
        }
    }

    results = pacientes.aggregate([ag1, ag2, ag3])

    for aux in results:
        print('Nome: ', aux["Nome"])
        print('Ano de Nascimento: ', aux["AnoNasc"])
        print('Dor: ', aux["Dor"])
        print('Leito: ', aux["Leito"])
        print('Sala: ', aux["Sala"])
        print('Analgesico: ', aux["Analgesico"])
        print("----------------------------")