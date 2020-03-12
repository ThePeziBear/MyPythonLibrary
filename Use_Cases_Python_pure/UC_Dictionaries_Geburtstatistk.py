#used methods: strip(). split(), items() function is used to iterator over (column name, Series) pair

# Aufgabe: Dictionaries Lese die ../data/names.csv - Datei ein und berechne, welcher Name insgesamt in den gesamten USA am häufigsten vergeben wurde.

with open("C:/Users/test/Documents/Udemy/Python/Kursmaterialien-2019/Kursmaterialien/data/names.csv", "r") as file:

    for line in file:
        print(line)
        break

    names = {}

    for line in file:
        splitted = line.strip().split(",") # WICHTIG! für Zugriff auf die einzelnen Spalten!!!
        if splitted[0] == "Id":
            continue

        surname = splitted[1] # Auswahl der zu zählenden Variable/Spalte
        count = int(splitted[5]) # Auswahl der zu zählenden Variable/Spalte

        # Überführung der Listeneinträge in ein Dictionary bei der ein KEY:VALUE zugewiesen wird
        # und jeder KEY
        if surname in names:
            names[surname] = names[surname] + count
        else:
            names[surname] = count

    max_occurences = 0
    #name = ""

# Suchen nach dem höchsten Namen
    for key, value in names.items():
        if max_occurences < value: #
            max_occurences = value
            name = key

    print(name)