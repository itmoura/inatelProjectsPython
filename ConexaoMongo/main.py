# Importando apenas um submodulo de uma lib
import pprint

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['aulaMongo']

country = db.aula

results = country.find({"region": "Europe", "area": {"$gt": 300000}}, {"name.common": 1, "_id": 0})

for aux in results:
    pprint.pprint(aux)

