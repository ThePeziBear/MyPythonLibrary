#import der Daten online und zip-extract

import urllib.request
import zipfile
import io

movieLensData = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
with urllib.request.urlopen(movieLensData) as f:
    zf = open('ml-100k.zip', 'wb')
    zf.write(f.read())
    zf.close()
    with zipfile.ZipFile('ml-100k.zip') as zipFileObj:
        zipFileObj.extractall(".")


# Auswahl Daten & Datenmanipulation
import pandas as pd
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
m_cols = ['movie_id', 'title']
movies = pd.read_csv('./ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
extra_data = [[0, 172, 5], [0, 133, 1], [0, 50, 5]]
ratings = ratings.append(pd.DataFrame(extra_data, columns=r_cols), ignore_index=True)
ratings = pd.merge(movies, ratings)


# Mit Hilfe der pivot_table - Funktion wird eine Tabelle erstellt, wo zu jedem Nutzer die entsprechenden Bewertungen der Filme definiert sind.
# NaN steht hierfür für fehlende Daten - also dass ein Nutzer diesen Film nicht bewertet hat
table=pd.pivot_table(ratings,values='rating',index='user_id',columns='title')


## Korrelation:
# Hier wird jeder Film mit den anderen Filmen korreliert. Daraus ergibt sich eine Korrelationsmatrix.
corr_matrix=table.corr()
# Für eine vernünftige Aussage, werden jetzt nur Filme mit 100 Nutzerbewertungen ausgwählt
corr_matrix_100=table.corr(method='pearson',min_periods=100)
corr_matrix_100.head()

# Auswahl Benutzer den wir weitere Film Vorschläge machen könnten.
myRatings = table.loc[0].dropna()


# Berechnungsalgorithmus für den Benutzer unter myRatings:
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    #print("Füge Ähnlichkeiten für " + str(myRatings.index[i]) + " hinzu...")
    # Berechne Filme, die ähnlich sind zu den Filmen die ich bewertet habe
    sims = corr_matrix_100[myRatings.index[i]].dropna()
    # Multipliziere den Ähnlichkeitswert mit meiner Bewertung
    sims = sims.map(lambda x: x * myRatings[i])
    # Und füge diesen Eintrag zur Liste hinzu
    simCandidates = simCandidates.append(sims)

## Ergebnismanipulation

#Sortierung der besten Ergebnisse - Es gibt jetz jedoch doppelte Einträge
simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head(10))

# Durch Gruppierung und Summierung sind keine weiteren doppelten Einträge vorhanden.
simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace = True, ascending = False)
simCandidates.head(10)

# Entfernen der bereits bewerteten Filme
filteredSims = simCandidates.drop(myRatings.index)
#ENDERGEBNIS!:
filteredSims.head(10)