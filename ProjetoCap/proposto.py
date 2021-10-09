import numpy as np
import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

# print(dfPaises['Region'])

oceania = dfPaises[dfPaises['Region'].str.contains("OCEANIA")]

# Exercicio 1
print("--- Paises da OCEANIA ---")
print(oceania['Country'])
print("--- Nº de Paises da OCEANIA ---")
print(oceania['Country'].count())

# Exercicio 2
print("\n")
print("--- Maior População ---")
population = dfPaises[dfPaises['Population']==dfPaises['Population'].max()]
print(population.filter(['Country', 'Region', 'Population']))

# Exercicio 3
print("\n")
print("--- Alfabetização por Região ---")
alfabetizacaoPorRegiao = dfPaises.groupby(['Region'], as_index=False)['Literacy (%)'].mean()
print(alfabetizacaoPorRegiao)

# Exercicio 4
print("\n")
print("--- Não possuem Costa Marítima ---")
noCoastFilter = dfPaises[dfPaises['Coastline (coast/area ratio)']==0]
noCoastFilter.to_csv('noCoast.csv', sep=';', header=True)
print("Gerado CSV")

# Exercicio 5
print("\n")
print("--- Taxa de Mortalidade ---")
dfPaises['Humanitarian Help'] = np.where(dfPaises['Deathrate'] < 9, "Balanced", "Urgent")
print(dfPaises)
dfPaises.to_csv('taxaMortalidade.csv', sep=';', header=True)