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