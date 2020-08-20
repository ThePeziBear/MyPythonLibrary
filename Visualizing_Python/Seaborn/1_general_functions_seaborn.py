import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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


#Funktion mit kategorischen Daten

#Barplots
sns.barplot(x="sex",y="total_bill",data=tips) #barplot erlaubt die kategorischen Daten einer Funktion zu aggregieren. Per Standard ist dies der Durchschnitt

sns.barplot(x="sex",y="total_bill",data=tips, estimator=np.std) # estimator definiert die Berechnungsfunktion z.B. Aggregation, Standardabweichung etc.

sns.countplot(x="sex",data=tips) #countplot ist das gleiche wie barblot, außer dass er die Anzahl an Ereignissen zählt


#Boxplots
sns.boxplot(x="day",y="total_bill",data=tips,palette="rainbow") # boxplots zeigen die Verteilung von kategorischen Daten.
                                                                # Die box zeigt die Quantile des Datensatzes.
                                                                # Das obere und untere Quantil ist der Median aus Minimumswert(untere Quantil) bzw. Maximumwert(oberes Quantil) und Median aus der Gesamtheit.
                                                                # Der Mittelwert oder Median der Gesamtheit ist in der Box der mittlere Strich. Die Punkte außerhalb des Plots sind Außreiser.

sns.boxplot(data=tips,palette="rainbow",orient="h") #orient 'h' lässt die Grafik auf horizontaler Ebene darstellen.

sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="coolwarm") #hue ermöglicht die grafische Darstellung von 2 Attributen (Smoker YES & Smokers No)


#Violinplot
sns.violinplot(x="day", y="total_bill", data=tips, palette="rainbow") # Anders als das box plot, in dem das Diagramm tatsächliche Datenpunkte repräsentiert,
                                                                      # zeigt das violin plot eine KDE (en. Kernal density estimation) der zugrundeliegenden Verteilung.

sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='rainbow')


#Stripplot & Swarmplot
sns.stripplot(x="day", y="total_bill", data=tips) # Das stripplot zeichnet ein Scatterplot, indem eine Variable katagorisch ist.
                                                  # Ein strip plot kann alleinstehend gezeichnet werden. Es passt aber auch gut zu einem box oder violin plot,
                                                  # wenn man neben der Verteilung auch alle einzelnen Datenpunkte visualisieren möchte.
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1') #Verwendung von Hue zur Darstellung von 2 verschiedenen Eigenschaften.


sns.swarmplot(x="day", y="total_bill", data=tips) # Der Unterschied zum Striplot liegt in der Anpassung der Punkte, so dass sie sich nicht überschneiden.
                                                  # Das gibt einen besseren Eindruck über die Verteilung der Punkte.
sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", dodge=True) #Verwendung von Hue zur Darstellung von 2 verschiedenen Eigenschaften.

#Kategorische Plots kombiniert!

sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)

plt.show()




