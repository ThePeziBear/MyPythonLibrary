######## Funktionen ########
# Funktionen sind zusammengefasste Codeblöcke. Mittels Funktionen können wir es vermeiden, mehrmals verwendete Codeblöcke zu wiederholen.
# Wir definieren stattdessen einmal eine Funktion, die diese Codeblöcke enthält und brauchen an weiteren Stellen nur noch (kurz) die Funktion aufzurufen, ohne die in ihr enthaltenen Codezeilen zu kopieren.

#Wenn wir eine eigene Funktion verwenden wollen, müssen wir sie zuerst definieren. Eine solche Funktionsdefinition hat die allgemeine Syntax:

def multi_print():
    print("Hallo Welt!")
    print("Hallo Welt!")

multi_print() # Ausgabe der Funktion


## Funktionen mit einem Argument ##
# Man kann Funktionen ein Argument übergeben, d. h. einen Wert, von dem der Code innerhalb der Funktion abhängt:

def multi_print2(name): # name ist z.B. das Argument welches definiert wird
    print(name)
    print(name)

multi_print2("HALLO") # HALLO ist das Argument welches 2 x Ausgegeben werden soll
multi_print2("WELT") # WELT ist das Argument welches 2 x Ausgegeben werden soll

## Funktionen mit mehreren Argumenten ##

# Eine Funktion darf auch mehrere Argumente enthalten.

## **def Funktionenname(Argument1, Argument2, ...):**

def multi_print(name, count):
    for i in range(0, count):
        print(name)

multi_print("Hallo!", 5)


## Funktionen in Funktionen ##
# Funktionen können auch ineinander geschachtelt werden:
def weitere_funktion():
    multi_print("Hallo!", 3)
    multi_print("Welt!", 3)

## Einen Wert zurückgeben ##
# Bislang führen wir mit Funktionen einen Codeblock aus, der von Argumenten abhängen kann. Funktionen können aber auch mittels des Befehls **return** Werte zurückgeben:
name = 0

def return_element(name):
    return name

print(return_element("Hi"))

# Solche Funktionen mit return können wir dann wie Variablen behandeln:

# V1
def return_with_exclamation(name):
    return name + "!"

if return_with_exclamation("Hi") == "Hi!":
    print("Right!")
else:
    print("Wrong.")

# V2
def maximum(a, b):
    if a < b:
        return b
    else:
        return a

result = maximum(4, 5)
print(result)

##################### Abschluss-Beispiele #####################

# Beispiel mit 2 Variablen und RETURN

def prices_list(name, price):
    p = []
    for i in range(1,11):
        p.append(str(i) + str(' x ') + name + ' : ' + str(price*i))
    return p

print(prices_list("Wunderkeks", 0.79))

# Beispiel: bei der ein Listeneintrag ersetzt wird mittels Methode

shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]

def add_shelf(article):
    for i in range (0,5):
        if shelf[i] == "leer":
            shelf[i] = article
            break

add_shelf("Rubik's Cube")
print(shelf)
