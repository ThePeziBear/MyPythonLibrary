import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,4], color = '#21c4ed', linestyle='dashed', marker='o')
# erste Liste die X-Werte, zweite Liste Y-Werte
# color via HEX - Farbe finden über color picker (google)
# allgemeine Infos = https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
#linestyle = https://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D.set_linestyle
# marker = https://matplotlib.org/api/markers_api.html#module-matplotlib.markers
plt.show() # Starten der Anzeige

# verschieden Diagrammtypen
plt.pie([1, 2, 3])
plt.show()

plt.bar([1, 2, 4], [5, 6, 5])
plt.show()

plt.scatter([1, 2, 4], [5, 6, 5])
plt.show()

plt.scatter([1, 2, 4], [5, 6, 5], color = "#ff0000", marker = "x")
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

#Erstellung von 2 oder mehreren Diagrammen in einem Output

diagramm, axes = plt.subplots(nrows = 1, ncols = 2) #diagramm ist variable & gibt das man ein Diagramm erstellen will;
# über axes werden die Anzahl der Plots definiert.

#Diagramm1
axes[0].plot(x,y)
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
#Diagramm2
axes[1].plot(y,x)
axes[1].set_ylabel('Y')
axes[1].set_xlabel('X')


diagramm
plt.tight_layout()
plt.show()


diag = plt.figure(figsize=(8,4),dpi=150) #DPI gibt die Auflösung und somit die Größe an.

ax= diag.add_axes([0,0,1,1])
ax.plot(x,y)


#Erstellen und Abspeichern einer Grafik als PNG-Datei
diag, axes=plt.subplots(figsize=(12,3),dpi=100) #DPI gibt die Auflösung und somit die Größe an.
axes.plot(x,y)
diag.savefig('dateiname.png', dpi=200) # Abspeichern einer Matplotlib Grafik