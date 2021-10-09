"""
    ÍTALO MOURA
"""

#importar a lib matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
# Criando um grafico de linahs no matplotlib
x = np.array([1,2,3,4])
y = x*2
y2 = x*x

# Mostrando o que temos em cada um dos eixos
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")

# Hora de plotar o grafico
plt.plot(x,y, 'o:g', x, y2,'o--r',linewidth=3, markersize=20)

# Mostrando o gráfico
plt.show()
'''



# plottar um scatterplot a partir de uma analise
# no dataset paises.csv
dfPaises = pd.read_csv('paises.csv', delimiter=';')

# Extraindo apenas os dados dos 6 maiores paises
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')

# Plotar um scatterplot deste paises
plt.scatter(
    x = dfPaises2['Country'],
    y = dfPaises2['GDP ($ per capita)'],
    s = dfPaises2['Population']/1000000
)

# Mostrando o gráfico
plt.show()

