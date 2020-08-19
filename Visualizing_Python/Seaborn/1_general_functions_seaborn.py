import seaborn as sns
#%matplotlib inline

tips = sns.load_dataset('tips')

#Verteilungsfunktion
sns.distplot(tips['total_bill'],kde=False #Anzeige der Dichtefunktion True
             , bins=10) #bins gibt die Anzahl der Klassen an


#Abhängigkeit von 2 Variablen
sns.jointplot(x='total_bill',y='tip',data=tips #Data = Auswahl Daten
              , kind='scatter')# kind = Dartellungsart

sns.jointplot(x='total_bill',y='tip',data=tips #Data = Auswahl Daten
              , kind='hex')# Hex ist tolle Darstellung für häufigsten Wert bei der Abhängigkeit von 2 Variablen.


sns.jointplot(x='total_bill',y='tip',data=tips #Data = Auswahl Daten
              , kind='kde')# Kernel Destiniy Darstellung tolle Darstellung für häufigsten Wert bei der Abhängigkeit von 2 Variablen

sns.pairplot(tips, #Das Diagramm pairplot zeigt paarweise Beziehungen in einem kompletten Dataframe. Für kategorische Variablen können wir über das hue Argument die Farbe einstellen.
             hue='sex',
             palette='coolwarm')