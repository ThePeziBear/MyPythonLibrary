import matplotlib.pyplot as plt

from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]

# Für die 10er Intervalschritte wurde eine Lambdafunktion mit //(nur ganze Zahlen bei Division) gewählt. Die Ausgabe wurde dann noch mit 10 mulitpliziert
decile = lambda grade: grade // 10 * 10

# Ausgabe der Anzahl der Noten die in das Decile reinfallen (4 Studenten fallen in den Intervall 80 etc.)
histogram = Counter(decile(grade) for grade in grades)

# Erstelle Histogram; die Zahl 8 gibt den Abstand der einzelnen Balken an.
plt.bar([x for x in histogram.keys()], histogram.values(), 8)

# Definition der Achsenbereiches
plt.axis([-5, 105, 0, 5])

# Bezeichnung der X-Achse in 10er Schritten
plt.xticks([10 * i for i in range(11)])

plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")

plt.show()
