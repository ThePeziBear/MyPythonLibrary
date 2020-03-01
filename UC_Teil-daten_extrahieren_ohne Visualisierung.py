# Aufgabe!
# Finde heraus, wie oft der Name "Max" als männlicher Vorname in Kalifornien zwischen 1950 und 2000 (jeweils einschließlich) vergeben wurde!
# Verwende dazu die bereitgestellte .csv - Datei (../data/names.csv)!

with open('C:/Users/test/Documents/Udemy/Python/Kursmaterialien-2019/Kursmaterialien/data/names.csv', 'r') as file:
    count = 0
    for line in file:
        list = line.strip().split(",")
        if list[1] == 'Max' and int(list[2]) >= 1950 and int(list[2]) <= 2000 and list[3] == 'M' and list[4] == 'CA':
            count = count + int(list[5])

print(count)
