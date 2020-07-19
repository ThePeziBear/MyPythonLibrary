#Verwendete Funktionen: Set(), Sort(), lambda

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

#Sortierung der Daten mit Lambda:
students = [
    ("Max", 3),
    ("Monika", 2),
    ("Erik", 3),
    ("Franziska", 1)
]

#Funktion ohne Lambda:
def students_key(i):
    return i[1]

students.sort(key=students_key)
print (students)

#Beispiel für Funktion ohne Lambda
tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]

def summe(x): # Berechnung Summe von element --> 10+2
    for element in x:
        s = x[0]+x[1]
        return s
summe(tupels) #ACHTUNG: Ausgabe jedoch nur von den ersten 2 Einträgen

tupels.sort(key = summe) #ACHTUNG: durch die Sort-Funktionen werden alle Einträge von "tupels" sortiert.

print(tupels)


#Beispiel 2 für Funktion ohne Lambda
names = ["Elif Else", "Sebastian Klarnamen", "Anna Boa", "Anton Adel", "Conny Coder", "Anne Wortmann", "Willy Cordes"]

def names_key(i):
    return i.split()[1] #Splitfunktion bezieht sich auf das 2. Element

names.sort(key=names_key)
print(names)


#Funktion mit Lambda --> kompakte Schreibweise da ich keine seperate Funktion anlegen muss
students.sort(key=lambda i: i[1])
print(students)



#Beispiel für Funktion ohne Lambda
tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]
tupels.sort(key=lambda i: i[0]+i[1])
tupels

