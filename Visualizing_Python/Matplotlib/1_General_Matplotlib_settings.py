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

###Erstellung von 2 oder mehreren Diagrammen in einem Output

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


###Erstellen und Abspeichern einer Grafik als PNG-Datei
diag, axes=plt.subplots(figsize=(12,3),dpi=100) #DPI gibt die Auflösung und somit die Größe an.
axes.plot(x,y)
diag.savefig('dateiname.png', dpi=200) # Abspeichern einer Matplotlib Grafik

### Legende erstellen bzw. Positionierung der Legende
diag = plt.figure()
ax=diag.add_axes([0,0,1,1])
ax.plot(x,x**2, label = 'x**2')
ax.plot(x,x**3, label = 'x**3')
ax.legend(loc=5) # Über loc 1-10 wird die Position der Legende bestimmt

### Grafik Formatierung (Farbe, Formen)

#Übersicht über alle Einstellungsmöglichkeiten:

diag, ax=plt.subplots()
ax.plot(x, x**2, color='#F4A460'# RGB Hex Code für color definieren Syntax:#Code
        ,alpha=0.9 # Transparenz Setting
        ,lw=1.5 # Dicke der Linie
        ,ls='--' # Art der Linie (gestrichelt, durchgehend)
        ,marker='o'# Setzen von Punkte auf der Linie
        ,markersize=10 #Größe der Marker
        ,markerfacecolor='yellow'#Farbe des markes
        ,markeredgewidth=3#Umrandungsdicke
        ,markeredgecolor='green')#Umrandungsfarbe

ax.set_xlim([0,4.5]) # Auswahl des Darstellungsbereichs von der X-Achse
ax.set_ylim([0,20]) #Auswahl des Darstellungsbereichs von der Y-Achse


#Example für verschiedene Linienformatierungen
diag, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# Mögliche Linienstile ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# Benutzerdefinierte Querstrich
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # Format: Linienlänge, Abstandslänge, ...

# Mögliche Markierungen: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# Markierungsgröße und Farbe
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");

plt.show()

#http://www.matplotlib.org - Die Webseite von Matplotlib.
#https://github.com/matplotlib/matplotlib - Der Sourcecode zu Matplotlib.
#http://matplotlib.org/gallery.html - Eine große Galerie, die viele Arten von Diagrammen zeigt, die mit Matplotlib erstellbar sind.