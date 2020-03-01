##### Listen in Python #####

### Algemein
# Über den + Operator kannst du 2 Listen miteinander verknüpfen!

students = ["Max", "Monika", "Erik", "Franziska"] + ["ABCDEF"]
print(students)

# Entefernen von Elementen in einer Liste

# V1:
students = ["Max", "Monika", "Erik", "Franziska", "ABCDEF"]
del students[3]
print(students)

# V2:
students = ["Max", "Monika", "Erik", "Franziska", "ABCDEF"]
students.remove("Monika")
print(students)


### List Slicing

students = ["Max", "Monika", "Erik", "Franziska", "ABC"]

print(students[-1]) # Ausgabe: ABC
print(students[-2]) # Ausgabe: Franziska
print(students[2:4]) # Ausgabe: Erik Franziska
print(students[1:-1]) # Ausgabe: Monika Erik Franziska
print(students[0:-1]) # Ausgabe: Max Monika Erik Franziska
print(students[:-1]) # Ausgabe: Max Monika Erik Franziska
print(students[1:])# Ausgabe: Monika Erik Franziska ABC


# List Slicing funktioniert auf auf Strings!

print("Hallo Welt"[0:5]) # Ausgabe: Hallo
print("Hallo Welt"[-4:]) # Ausgabe: Welt
print("Hallo Welt"[1:5]) # Ausgabe alo

### List Comprehension


# Variante ohne List Comprehension
# Bsp.1
xs = [1, 2, 3, 4, 5, 6, 7, 8]
yt = []
for element in xs:
    yt.append(element * element)
print(yt)

# Bsp.2
students = ["Max", "Monika", "Erik", "Franziska"]
lengths = []
for element in students:
   lengths.append(len(element))

print(lengths)



# Variante mit List Comprehension

# Bsp.1
xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [element * element for element in xs]

print(xs)
print(ys)

# Bsp.2
students = ["Max", "Monika", "Erik", "Franziska"]
lengths = [len(element) for element in students]
print(lengths)

# Listen verschachtelt

liste = [
    ["Berlin", "München", "Köln"],
    ["Budapest", "Pécs", "Sopron"]
]
print(liste[0][0]) # Zugriff auf die erste Liste auf den ersten Eintrag
print(liste[1][2]) # Zugriff auf die zweite Liste auf den letzten Eintrag


# Listen in Dictionaries

students = {
    "Informatik": ["Max", "Monika"],
    "BWL": ["Erik", "Franziska"]
}

print(students["Informatik"])
print(students["BWL"])





