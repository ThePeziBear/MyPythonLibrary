
## TXT -DATEI ##

# Wir öffnen die Datei lesen.txt zum Lesen ("r") und speichern ihren Inhalt in die Variable file
file = open("lesen.txt", "r") # wird "w" anstelle "r" definiert, dann kann man datei auch verändern

# Wir gehen alle Zeilen nacheinander durch
# In der txt-Datei stehen für uns nicht sichtbare Zeilenumbruchszeichen, durch die jeweils das Ende einer Zeile markiert ist
for line in file:
    print(line.strip()) # Eine Zeile ohne Zeilenumbruch ausgeben

## CSV -DATEI ##

# CSV lesen
with open("datei.csv") as file: # Wir öffnen die Datei "datei.csv"  und speichern ihren Inhalt in die Variable file
    for line in file: # Jede Zeile wird mit For-Schleife aufgerufen
        data = line.strip().split(";") # Zeile ohne Zeilenumbruch & split-Funktion um ; zu elemenieren
        print(data[0] + ": " + data[1]) # Ausgabe von 1. Eintrag der Liste + :-(string) + 2. Eintrag der Liste


# CSV lesen und Daten überspringen

with open("datei.csv") as file:  # Wir öffnen die Datei "datei.csv"  und speichern ihren Inhalt in die Variable file
    for line in file: # Jede Zeile wird mit For-Schleife aufgerufen
        data = line.strip().split(";") # Zeile ohne Zeilenumbruch & split-Funktion um ; zu elemenieren
        if int(data[1]) < 2000000: #überspringen bei Stadt weniger als 2.Mio Einwohner
            continue

        if data[2] == "BUD": # überspringen wenn die Bezeichnung "BUD" gegeben ist.
            continue

        print(data)

# CSV lesen und die ersten 5 Einträge darstellen:

with open("../data/names.csv", "r") as file:
    counter = 0
    for line in file: # jede zeile wird durchgegangen
        counter = counter + 1
        print(line)
        if counter >= 6:
            break

# CSV lesen mittels Pandas
import pandas as pd
df = pd.read_csv("C:/Users/test/Documents/Udemy/Python/Kursmaterialien-2019/Kursmaterialien/data/astronauts.csv")

## EXCEL - DATEI ##
# EXCEL-Importfunktion kann noch viel mehr - z.B einzelne Tabellenblätter auslesen etc....
df = pd.read_excel("C:/Users/test/Documents/Udemy/Python/Kursmaterialien-2019/Kursmaterialien/data/daten.xlsx")
print(df.head())


## Zip Datei einlesen ##

import zipfile
import urllib.request
import shutil

url = 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
file_name = 'ml-100k.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()

print(pd.read_csv('./ml-100k/u.data',sep='\t'))


