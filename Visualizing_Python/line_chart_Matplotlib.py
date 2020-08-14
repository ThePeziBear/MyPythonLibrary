import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# erstelle Linienchart. years = x-Achse= years, y-Achse = GDP, marker = Dartellung der Punkte als kreise, linestyle = durchgehend
plt.plot(years, gdp, color='blue', marker='o', linestyle='solid')

# Titel hinzufügen ('Titel')
plt.title("Nominal GDP")

# hinzufügen einer Beschriftung der Y-Achse
plt.ylabel("Billions of $")

#Darstellung des Plots

plt.show()


# Objektorientierte Erstellung eins Diagramms mit einer eingesestzten Grafik

import numpy as np

x = np.linspace(0,5,11)
y = x**2

af = plt.figure() #Diagramm erstellen (leere Arbeitsfläche)
axes1 = af.add_axes([0.1,0.1,0.8,0.8]) # Positionierung der Grafik
axes2 = af.add_axes([0.2,0.5,0.4,0.3]) # Positionierung der eingesetzten Grafik

# Großes Diagramm
axes1.plot(x,y,'b')
axes1.set_xlabel('X') # Achsenbezeichnung x
axes1.set_xlabel('Y') # Achsenbezeichnung Y
axes1.set_title('big diagramm') #Diagramm - Titel

# Eingesetztes Diagramm mit Achse 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('X') # Achsenbezeichnung x
axes2.set_xlabel('Y') # Achsenbezeichnung Y
axes2.set_title('small diagramm') #Diagramm - Titel

plt.show()