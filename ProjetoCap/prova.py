"""
    PROVA 2 - C111
    AUTHOR: ÍTALO MOURA

"""

import matplotlib.pyplot as plt
import pandas as pd

# no dataset rio.csv
dfRio = pd.read_csv('rio.csv', delimiter=',')


# QUESTÃO 1
# Search sex male
homens = dfRio[dfRio['sex'].isin(['male'])].stack()
# Search sex female
mulheres = dfRio[dfRio['sex'].isin(['female'])].stack()

homensCont = homens.count()
mulheresCont = mulheres.count()

maleBar = plt.bar("Masculino", homensCont, width=0.5, color='blue', align='center')
femaleBar = plt.bar("Feminino", mulheresCont, width=0.5, color='pink', align='center')
plt.title('Sexo dos atletas que participaram do evento')
plt.legend( (maleBar[0], femaleBar[0]), ('Sexo Masculino', 'Sexo Feminino') )

plt.show()

# QUESTÃO 2
print("--- QUESTÃO 2 ---")
atletasPesados = dfRio[dfRio['weight'] >= 150]
atletasPesadosCont = atletasPesados.count()
print(atletasPesados['sport'].unique())
print('\n')

# QUESTÃO 3
print("--- QUESTÃO 3 ---")
medalhista = dfRio.sort_values(by=['gold'], ascending=False, ignore_index=True)
print("Nome: ", medalhista['name'].get(0))
print("Nacionalidade: ", medalhista['nationality'].get(0))
print("Esporte: ", medalhista['sport'].get(0))
print('\n')

# Questão 4
print("--- QUESTÃO 4 ---")
volley = dfRio[dfRio['sport']=='volleyball']
volleyAndFemale = volley[volley['sex']=='female']
print("Altura média: ", volleyAndFemale['height'].mean())
print('\n')

# Questão 5
print("--- QUESTÃO 5 ---")
nacionalidade = dfRio.groupby('nationality').count()
nacionalidade = nacionalidade.sort_values(by='id', ascending=False)
nacionalidade = nacionalidade[:3]
print(nacionalidade['id'])

plt.pie(x=nacionalidade['id'], labels=nacionalidade.index, shadow=True, explode=[0, 0.1, 0], autopct='%1.1f%%', colors=['blue', 'green', 'pink'])
plt.title("Paises com mais atletas")
plt.gca().legend((nacionalidade['id']), loc=2)
plt.show()
