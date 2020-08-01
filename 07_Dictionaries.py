# ## Dictionaries in Python
# - Du kannst Wertezuordnungen speichern (z. B. Telefonbuch: Ein Nachname hat eine Telefonnummer).
# - Du kannst nachträglich Elemente verändern / entfernen / hinzufügen.
# - Dictionaries brauchst du wirklich immer wieder...

d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}

print(d)
#Ausgabe: {'Berlin': 'BER', 'Helsinki': 'HEL', 'Saigon': 'SGN'}

print(d["Helsinki"])
#Ausgabe: HEL

## Element einfügen
d["Budapest"] = "BUD" # Einfügen eines Dictionaries-Eintrag

print(d)
#Ausgabe: {'Berlin': 'BER', 'Helsinki': 'HEL', 'Saigon': 'SGN', 'Budapest': 'BUD'}


## Element entfernen

del d["Budapest"]

print(d)
#Ausgabe: {'Berlin': 'BER', 'Helsinki': 'HEL', 'Saigon': 'SGN'}

## Abfrage: Ist ein Element im Dictionary?

if "Budapest" in d:
    print("Budapest ist im Dictionary enthalten")
if "Saigon" in d:
    print("Saigon ist im Dicionary enthalten")


## Auf Elemente zugreifen...



# V1 - hier bekomme ich einen Fehler zurück
print(d["Saigon"])
print(d["Budapest"]) # Fehler bei Budapest

#V 2 - hier bekomme ich eine None zurück
print(d.get("Saigon"))
print(d.get("Budapest")) # Hier bekomme ich ein None zurück



#Aufgabe: PriorityQueue¶
#Ermittle den 5.-häufigsten Vornamen, der in den USA vergeben wurde! Lies dazu die ../data/names.csv - Datei ein.
# Verwende dazu zuerst ein Dictionary, mit dem du die Häufigkeit der Vornamen zählst und anschließend eine PriorityQueue, um die Top 5 Vornamen zu ermitteln.

with open("../data/names.csv") as file:
    namelist=[]
    for line in file:
        datalist=line.strip().split(",")
        namelist.append(datalist)


names=[]
for line in namelist:
    data=line[1]
    names.append(data)

names


d={}

for element in names:
    if element in d:
        d[element] = d[element]+1
    else:
        d[element]=1

import queue

q = queue.PriorityQueue()

for element, number in d.items():
    q.put((-number, element))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())


#Verwendung Format() - Funktion

planet = "Erde"
durchschnitt = 12742

" Der Durchschnitt der {} ist {} Kilometer.".format(planet,durchschnitt)