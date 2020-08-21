import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
tips = sns.load_dataset('tips')
fluege = sns.load_dataset('flights')

###Matrixplots###

#Heatmap
#Damit die Heatmap gut funktioniert sollten eure Daten bereits in Matrixform vorliegen. Die sns.heatmatp() übernimmt dann die Einfärbung dieser Daten

# Matrix der Korrelationsdaten
tips.corr() #corr Funktion erkennt automatisch numerische Spalten & lässt kategorische Spalten weg.


sns.heatmap(tips.corr()) #Ausführen der Heatmap aufgrun der Korrelationsverteilung
plt.show()

sns.heatmap(tips.corr(),cmap='coolwarm',annot=True) # cmap: Farbvariante, annot: Korrelationswerte in dem Kästschen
plt.show()

#Erstellung einer Pivottabelle für die Darstellung der Daten in Jahre
pvfluege = fluege.pivot_table(values='passengers',index='month',columns='year') #values: Anzahl der der Passagiere; Index: sind die Zeilen, columns: sind die Spalten

sns.heatmap(pvfluege,cmap='magma',linecolor='white',linewidths=1) # linecolor: lässt eine Unterteilung zu; linewidths: gibt die Linienstärke wieder.
plt.show()

#Clustermap: welche Kategorien(z.B. Monate an dene geflogen werden) liegen beieiander

sns.clustermap(pvfluege,cmap='coolwarm',standard_scale=1) # standard_scale: Dimension für die Zeile oder für die Spalte standardisieren möchten (Subtrahieren von jedem Wert durch Minimum und anschließend Division jedes Wertes durch Maximum
plt.show()                                                # Für Standardisierung von Zeilen  0 und für Spalten 1.


#Regressionsplots:

sns.lmplot(x="total_bill",y="tip", data=tips) # Vergleich von Bill mit Tip bzgl. Korrelation
plt.show()

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',#hue: Trennung von kategorischen Parameter
            markers=['o','v'], #Veränderung der Symbole
            scatter_kws={'s':100}) #scatter_kws: Definition von der Göße der Symbole
plt.show()


sns.lmplot(x='total_bill',y='tip',data=tips, row='time', col='sex') #über row & col können multiple Korrelationsgrafiken erstellt werden.
plt.show()