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
plt.show

plt.scatter([1, 2, 4], [5, 6, 5])
plt.show()

plt.scatter([1, 2, 4], [5, 6, 5], color = "#ff0000", marker = "x")
plt.show()