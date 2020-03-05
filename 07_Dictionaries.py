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

