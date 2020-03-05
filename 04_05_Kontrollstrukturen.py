## IF-ELIF-ELSE ##
# Wir können in einer if-else-Struktur nur zwei Fälle abfragen, nämlich, ob eine Bedingung wahr ist (True) oder nicht (False).
# Wenn wir ein Entscheidungsmodell programmieren wollen, in dem noch mehr Bedingungen gecheckt werden sollen, müssen wir bislang mehrere if-else-Strukturen ineinander verschachteln.

currency = "€"

if currency == "$":
    print("US-Dollar")
else:
    if currency == "¥":
        print("Japanischer Yen")
    else:
        if currency == "€":
            print("Euro")
        else:
            if currency == "฿":
                print("Thai Baht")


# Durch die Erweiterung um elif können wir innerhalb einer if-else-Struktur beliebig viele Bedingungen checken.

# elif ist die Kurzfassung von else if
# Eine elif-Option deckt also den Fall ab, dass die if-Bedingung nicht erfüllt (False) ist, aber eine weitere Bedingung True ist.

currency = "HKD"

if currency == "$":
    print("US-Dollar")
elif currency == "¥":
    print("Japanischer Yen")
elif currency == "€":
    print("Euro")
elif currency == "฿":
    print("Thai Baht")
else:
    print("Sonst")

## SCHLEIFE ##
# Ein Code-Block innerhalb einer if-elif-else-Struktur wird jeweils nur einmal ausgeführt.
# Bei Schleifen wie der while-Schleife wird ein Code-Block so lange mehrmals hintereinander ausgeführt, bis eine Abbruchbedingung erfüllt ist.

## WHILE SCHLEIFE ##

# Innerhalb einer Schleife muss sich unbedingt ein Zustand in jedem Schritt verändern, damit die Schleifenbedingung nicht dauerhaft erfüllt ist,
# und das Programm die Schleife auch wieder verlassen kann:
students = ["Moritz", "Klara", "Monika", "Max"]
i = 0
while i < len(students): # len-Funktion:  Anzahl aller Einträge wird durchgegangen und dann ist Schleife beendet
    print(students[i])
    i = i + 1


## FOR SCHLEIFE ##

# Neben der while-Schleife, die wir schon kennen gelernt haben, gibt es noch die for-Schleife.
# Hier durchläuft eine Schleifenvariable nacheinander die Werte in einer ebenfalls anzugebenden Sequenz.

liste = ["Max", "Moritz", "Monika"]
for i in liste:
    print(i)

# Das range-Objekt
# Als Sequenz für eine for-Schleife braucht man nicht zwangsläufig eine Liste. Häufig greift man stattdessen auf ein **range**-Objekt zurück:

# Hier summieren wir alle Zahlen von 1 bis 10 mithilfe einer for-Schleife und eines range-Objektes auf
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

# Wann welche Schleife?
# While Schleife verwenden wenn der Zahlenbereich nicht bekannt ist.
# Ansonsten for Schleife - da diese weniger Fehler produziert im Ausführen.

## Schleifen (break, continue)##
# Continue & Break
# Wir können während eines Schleifendurchlaufs den aktuellen Durchlauf vorzeitig abbrechen und unmittelbar mit dem nächsten Schleifendurchlauf fortfahren (continue) oder auch die gesamte Schleife abbrechen (break).


##################### Abschluss-Beispiele #####################

# 1. Aufgabe: Kontinente - For Schleife
# a.) Gib nacheinander alle Kontinente aus der Liste continents aus.

continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

for i in continents:
    print(i)

# b.) Gib aus der Liste continents nur die bewohnten Kontinente aus. - For Schleife mit if-Funktion
# Hinweis:: Antarktis ist nicht bewohnt. Diesen Kontinent kannst du also bei der Ausgabe einfach überspringen.

for i in continents:
    if i == "Antarktis":
        continue
    print(i)

# c.) Gib aus der Liste stuff nur die Kontinente aus - For Schleife mit IF-Funktion und IN-Operator
# Du kannst dafür die Liste stuff mit einer Schleife durchgehen und dann mit Hilfe der Variable continents prüfen, ob ein Element der Liste stuff auch in der Liste continents vorkommt.

stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]

for i in stuff:
    if i in stuff and i in continents:
        print (i)


# d.) Wie viele Kontinente sind in der Liste `stuff` enthalten? - For Schleife mit IF-Funktion und IN-Operator

count = 0

for i in stuff:
    if i in continents:
        count = count + 1
print(count)


# 2. Aufgabe: Rabattaktion
# Zurück zur Mathemagierin: Sie möchte in ihrem Shop eine Rabattaktion starten, um das Geschäft anzukurbeln. Natürlich hat sie dabei wieder etwas zu programmieren für dich. Du sollst die Berechnung der reduzierten Preise mit einer if-elif-else-Struktur vereinfachen.

# Dabei ist zu beachten:
# Artikel, die zwischen 0 und 20 (einschließlich) Taler kosten, werden um 20 % reduziert; Artikel, die zwischen 20 (nicht einschließlich) und 50 Taler (einschließlich) kosten, werden um 40 % reduziert. Alle anderen Artikel, also solche, die mehr als 50 Taler kosten, werden um 60 % reduziert.

#a.) Gib für die Variable price den neuen, rabattierten Preis aus. IF-ELIF-ELSE Struktur

price = 50

if price <= 20:
    price = price * 0.8
elif price <=50:
    price = price * 0.6
else:
    price = price * 0.4

print(price)

# b.) Berechne nun für jeden der alten Preise aus der Liste prices die passenden reduzierten Preise und speichere sie in der neuen Liste new_prices. Gib diese Liste schließlich aus.
# For Schleife mit IF-ELIF-ELSE Struktur & append Funktion
prices = [2, 50, 70, 30]
new_prices = []

for i in prices:
    if i <= 20:
        i = i * 0.8
    elif i <= 50:
        i = i * 0.6
    else:
        i = i * 0.4

    new_prices.append(i)

print(new_prices)

# c.) Zusatzaufgabe (schwierig!)
# Nun überreicht dir die Mathemagierin mit zitternden Händen die Liste chaos, in der neue und alte Preise gemischt sind! Angesichts dieser undurchdachten Arbeit schlägst du dir die Hände vor dem Kopf zusammen, aber es hilft ja nichts: Nur du kannst hier wieder Ordnung schaffen, indem du alles zusammenbringst, was du schon gelernt hast!

# Gehe die Elemente in der Liste chaos durch. Bei einem neuen Preis ziehst du bloß den neuen Wert aus dem String und hängst ihn der Liste order an. Bei einem alten Preis hingegen holst du dir den alten Wert, berechnest den neuen Preis und hängst diesen Wert an die Liste order.

# Schließlich gibst du die vollständige Liste order aus, in der nur noch neue Preise drinstehen (und nur noch Zahlen!). # For Schleife mit IF-ELIF-ELSE Struktur & append Funktion

chaos = ["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for i in chaos:

    price = int((i.split(": ")[1]))

    if "old" in i:
        if price <= 20:
            price *= 0.8
        elif price <= 50:
            price *= 0.6
        else:
            price *= 0.4

    order.append(price)

print(order)