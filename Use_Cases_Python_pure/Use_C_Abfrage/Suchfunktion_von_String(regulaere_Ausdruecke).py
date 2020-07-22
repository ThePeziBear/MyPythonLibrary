# Reguläre Ausdrücke erlauben es, Strings noch flexibler zu durchsuchen.
# Beispielsweise kann man mit einem regulären Ausdruck alle Zahlen in einem String finden oder validieren, dass eine E-Mail-Adresse grundsätzlich existieren könnte.

import re

sentence = "Ich habe 30 Hunde, die jeweils 4 Liter Wasser brauchen und 2 kg Nahrung."
re.findall("[0-9]+", sentence) # Finde alle Zahlen zwischen 0 & 9. Das + bedeutet, dass auch eine weitere Zahl erkannt wird z.B. 3 und 30

re.search("der?", "Hallo der Hallo") # Das ? definiert dass das r optional ist

print(re.search("der*", "Hallo de Hallo")) # Das * definiert, dass das r optional ist.
print(re.search("der*", "Hallo der Hallo"))
print(re.search("der*", "Hallo derrrrrrrr Hallo")) # Das * definiert, auch dass nach dem r beliebig viele andere r optional sind.

#WICHTIG: https://regexr.com/ - Cheatsheets bzw. Erklärungen von Suchabfragen
