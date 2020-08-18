import seaborn as sns
#%matplotlib inline

tips = sns.load_dataset('tips')

#Verteilungsfunktion
sns.distplot(tips['total_bill'],kde=False #Anzeige der Dichtefunktion True
             , bins=10) #bins gibt die Anzahl der Klassen an


#Abhängigkeit von 2 Variablen
sns.jointplot(x='total_bill',y='tip',data=tips #Data = Auswahl Daten
              , kind='scatter')# kind = Dartellungsart

