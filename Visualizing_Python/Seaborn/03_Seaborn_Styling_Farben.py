import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')

sns.set_style('ticks')# Auswahl vom Diagrammhintergrund
plt.figure(figsize=(12,3)) # Definition von der Größe des Diagramms

sns.countplot(x='sex',data=tips,palette='deep')
sns.despine(left=True) #Löschen vom Diagrammrahmen; Zeileninhalt(z.B: left=True) können noch weitere Linien ausgeblendet werden

sns.set_context('paper',font_scale=2) #set_context ermöglicht die Standard Skalierungsdarstellung zu überschreiben
                                      # paper, talk, poster etc. sind angepasste Darstellungsvarianten.
                                      #font_scale definiert die größe der Darstellung
sns.countplot(x='sex',data=tips,palette='GnBu')

# https://matplotlib.org/tutorials/colors/colormaps.html Website für die verschiedenen Farbpaletten.