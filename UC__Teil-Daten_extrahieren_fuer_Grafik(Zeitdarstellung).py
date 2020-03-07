#used Methods: strip(), list(). append

# Beispiel: Geburtstatistik
# Es wird aus einem großen Datensatz eine Teilmenge extrahiert für eine grafische Aufbereitung OHNE PANDAS.
import matplotlib

xs = []
ys = []

name = "Anna"
gender = "F"
state = "CA"

with open("C:/Users/test/Documents/Udemy/Python/Kursmaterialien-2019/Kursmaterialien/data/names.csv", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1

        line_splitted = line.strip().split(",") # Entfernung Absatzeichen (strip-Methode) & Überführung Lines in List-Einträge
        if line_splitted[1] == name and line_splitted[3] == gender and line_splitted[4] == state: # Abfrage der oben definierten Variablen
            xs.append(line_splitted[2]) # Anhängen der abgefragten Variablen in die leere Liste
            ys.append(line_splitted[5]) # Anhängen der abgefragten Variablen in die leere Liste
            #print(line_splitted)
            #break

print(xs)
print(ys)

#%matplotlib.inline - funktioniert im Pycharm nicht - verwende Jypiter Notebook
import matplotlib.pyplot as plt

plt.plot(xs, ys)
plt.show()



