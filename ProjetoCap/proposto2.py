import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# no dataset paises.csv
dfSpace = pd.read_csv('space.csv', delimiter=';')

usa = dfSpace[dfSpace['Location'].str.contains("USA")]
china = dfSpace[dfSpace['Location'].str.contains("China")]

usaCont = usa.count().unique()
chinaCont = china.count().unique()

# Plotar um scatterplot deste paises
usaBar = plt.bar("USA", usaCont, width=0.5, color='blue', align='center')
chinaBar = plt.bar("China", chinaCont, width=0.5, color='red', align='center')
plt.title('Empresas Espaciais nos Países')
plt.legend( (usaBar[0], chinaBar[0]), ('Estados Unidos', 'China') )

plt.show()


#------------------------
# Exercicio 2
dfPaises = pd.read_csv('paises.csv', delimiter=';')

americaNorte = dfPaises[dfPaises['Region'].str.contains("NORTHERN AMERICA")]

amercaNorteDeathrate = np.array(americaNorte['Deathrate'])
amercaNorteBirthrate = np.array(americaNorte['Birthrate'])
amercaNorteDeathrate.sort()
amercaNorteBirthrate.sort()

americaNorteCont = americaNorte.count().unique()
x = np.array([0])
i = 1
while i < americaNorteCont:
    x = np.append(x, i)
    i += 1

x = plt.plot(x, amercaNorteDeathrate, 'r-', x, amercaNorteBirthrate,'b--')
plt.title('Taxa de Mortalidade e Natalidade da America do Norte')
plt.gca().legend(('Mortalidade','Natalidade'))

# Mostrando o gráfico
plt.show()