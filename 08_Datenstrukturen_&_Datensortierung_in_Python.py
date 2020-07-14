#Verwendete Funktionen: Set(), Sort()

#Set - Bei Versuch noch einen 2. gleichen Eintrag hinzuzufügen wird dieser Befehl nicht ausgeführt.
s={"Hallo","Welt"}
s.add('Mars')#hinzufügen von einem Eintrag
print(s)

text="Hallo Welt Hallo Mars Hallo Welt"
words=set()
for i in text.split(' '):
    words.add(i)

print(words)

#**Aufgabe:**

#Öffne die ../data/names.csv - Datei als .csv-Datei und berechne die Anzahl der verschiedenen Vornamen, die in dieser Datei aufgelistet sind!
import csv
with open('C:/Users/test/Documents/Udemy/Python/Kursmaterialien-2019/Kursmaterialien/data/names.csv') as file:
    names=set() # erstellen einer Set-Funktion
    for line in file:
        data=line.strip().split(",") # splitten der Einträge
        names.add(data[1])
    print(names)
    print(len(names))


####Sortierung von Daten####

#Sortierung von Daten in einer Liste

l = ["Max", "Monika", "Erik", "Franziska"]
l.sort() # Sortiert die Daten aufsteigend
print(l)

l = ["Max", "Monika", "Erik", "Franziska"]
l.sort(reverse=True)  # Sortiert die Daten absteigendsteigend
print(l)


def get_length(item): # Sortierung der Daten nach eigenem Kriterium z.B. nach der Namenslänge
    return len(item)
l = ["Max", "Monika", "Erik", "Franziska"]
l.sort(key=get_length)
print(l)

l = ["Max", "Monika", "Erik", "Franziska"]
l.sort(key=len) # Alternative schreibweise für die Sortierung nach Namenslänge
print(l)


#Sortierung von Daten nach einem Dictionary
d = {"Köln": "CGN", "Budapest": "BUD", "Saigon": "SGN"}
print(sorted(d, reverse = True))
