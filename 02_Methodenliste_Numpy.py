## Numpy ##
import numpy as np

## Arrays erzeugen

# Mit dem `array()` - Befehl können wir Python-Listen in Arrays umwandeln.
print(np.array([1, 2, 3, 4, 5, 10]))

# Mit der `arange()` - Funktion wird ein Array zu einem beliebigen Zahlenbereich erstellt.

print(np.arange(1, 11))

print(np.arange(10))

# Es gibt auch einen eigenen Befehl um einen beliebig langen Array zu erzeugen (hier: 10 Elemente), der nur mit Nullen gefüllt ist: die `zeros()`-Funktion.

print(np.zeros(10))

# Mit `ones()` gibt es eine entsprechende Funktion auch für Einsen:

print(np.ones(10))

## Mit Arrays rechnen
# Rechenoperationen auf einem Array-Objekt werden für jeden Wert des Arrays ausgeführt, ohne dass diese Werte in einer _Schleife_ oder _list comprehension_ ausdrücklich durchlaufen werden müssen.

print(np.arange(10) + 3)

print(np.arange(10) * 3)

## vorgefertigte Methoden für Arrays:

# Mittelwert
print(np.array([1, 2, 3, 4, 5, 10]).mean())

# Minimum
print(np.array([1, 2, 3, 4, 5, 10]).min())

# Maximum
print(np.array([1, 2, 3, 4, 5, 10]).max())

# Standardabweichung
print(np.array([1, 2, 3, 4, 5, 10]).std())


## Ein Array mit einem anderen Array filtern

# Wir können ein Array mit Boolean - Einträgen dazu verwenden, ein anderes Array zu filtern.

a = np.array([1, 2, 3, 4])
print(a)

# Wir können spezifischer filtern, indem wir Vergleiche für Arrays formulieren.
# Wie die Rechenoperationen werden auch die Vergleichsoperationen auf jeden Wert eines Arrays angewendet - jeder Wert wird einzeln verglichen:

c = a >= 3  # ersetzt die for-schleife
print(c)

a_filterd_3 = a[a >= 3]
print(a_filterd_3)


## Reshape

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a)


a.reshape((2, 4)) # Jede der Zahlen in dem Tupel steht dafür, wie viele Elemente es in einer Dimension geben soll.


# Mit dem Parameter `(2, 4)` wird definiert, das bei 2
# dass das äußere Arry zwei sagen wir also, dass der äußere Array zwei Elemente enthalten soll (d.h. zwei Unter-Arrays), und die Arrays der zweiten Stufe jeweils vier Elemente enthalten sollen (d.h. die Werte).
#
# Bei zwei Dimensionen, d.h. einem Tupel mit zwei Elementen als Parameter, kannst du dir den ersten Wert des Tupels als Anzahl der Zeilen und den zweiten Wert als die Anzahl der Spalten vorstellen.

# Auf die Elemente in einem solchen mehrdimensionalen Array kannst du mit mehrfacher Verwendung der `[ ]-Schreibweise` zugreifen.

# In[22]:


reshaped = a.reshape((2, 4))

print(reshaped[0])
print(reshaped[0][0])
print(reshaped[1])
print(reshaped[1][3])


# Natürlich kannst du mit `reshape()` nur Verschachtelungen erzeugen, die zur Gesamtzahl der Einträge passen, d.h. das Produkt über alle Werte aus dem Tupel, das du als Parameter übergibst, und die Anzahl der Elemente aus dem Array müssen übereinstimmen.
#
# Sonst passiert das:

# In[23]:


c = np.array([1, 2, 3, 4, 5, 6, 7])
c.reshape((4, 2))


# ### Parameter-Platzhalter: Anzahl von Einträgen in einer Dimension offen lassen

# Du kannst auch **-1** als Platzhalter für die Anzahl der Einträge in einer Ebene benutzen, statt sie zu spezifizieren; Numpy füllt dann die neuen Unter-Arrays automatisch mit Einträgen auf.

# In[13]:


a.reshape((-1, 4))


# In[16]:


a.reshape((4, -1))


# So können wir schnell ein eindimensionales Array erzeugen:

# In[17]:


b = np.array([[1, 2, 3], [4, 5, 6]])
b.reshape(-1)


# ### Die Dimensionen eines Arrays abfragen
# Die Maße eines Arrays können wir mit der `shape`-Eigenschaft des Array-Objektes abfragen.

# In[21]:


b.shape



