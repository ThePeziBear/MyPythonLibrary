print('Mithilfe diesem Rechner kannst du ganz einfach deinen BMI ausrechnen)')
print('\nGebe dafür einfach dein Gewicht in kg und deine Körpergröße in cm ein.')

Gewicht = input('Bitte gebe dein Gewicht in kg ein:')
Körpergröße = input('Bitte gebe deine Körpergröße in cm ein:')

BMI_Wert = float(Gewicht)/(float(Körpergröße)/100*float(Körpergröße)/100)
print('\n')
print('Dein BMI-Wert: ' + str(BMI_Wert))

print ('\nKategorie	            BMI (kg/m²)	    Körpergewicht')
print ('Leichtes Untergewicht	17,0 - 18,5	    Untergewicht')
print ('Normalgewicht	        18,5 - 24,9	    Normalgewicht')
print ('Präadipositas	        25,0 - 29,9	    Übergewicht')
print ('Adipositas Grad I	    30,0 - 34,9     Adipositas')