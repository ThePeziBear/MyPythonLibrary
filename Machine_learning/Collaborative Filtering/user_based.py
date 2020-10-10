import zipfile
import urllib.request
import shutil

#import der Daten online und zip-extract
url = 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
file_name = 'ml-100k.zip'

with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()


# Auswahl Daten & Datenmanipulation
import pandas as pd
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
m_cols = ['movie_id', 'title']
movies = pd.read_csv('./ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
ratings= pd.merge(movies,ratings)
ratings.info()

# Mit Hilfe der pivot_table - Funktion wird eine Tabelle erstellt, wo zu jedem Nutzer die entsprechenden Bewertungen der Filme definiert sind.
# NaN steht hierfür für fehlende Daten - also dass ein Nutzer diesen Film nicht bewertet hat
table = pd.pivot_table(ratings,values='rating',index='user_id',columns='title',aggfunc='mean')

# Welche Nutzer haben Star Wars bewertet?
table_sw=table['Star Wars (1977)']


# Mit Hilfe der corrwith - Funktion von Pandas kann Korrelation von jedem Nutzer der Star Wars bewertet hat zu den anderen Filmen berechnet werden.
# Anschließend werden alle Einträge verworfen bei denen keine Werte definiert sind, und aus dem Ergebnis wird ein neues DataFrame erstellt,
# dieses enthält dann die Korrelation (Ähnlichkeit) zum Star Wars - Film
similarMovies=table.corrwith(table_sw)
similarMovies=similarMovies.dropna()
similarMovies=pd.DataFrame(similarMovies)

#Wenn man jetzt die Ergebnisse nach Ähnlichkeitswert sortiert, sollten oben die Filme stehen, die ähnlich zu Star Wars sind.
# Aufgrund der hohen Anzahl von Korrelationen um die 1 dürfte es sich hier um Ausreißer handeln.  Unsere Ergebnisse werden duch
# ein paar Filme beeinflusst die von nur wenigen Benutzern gesehen wurden. Diese Ausreißer müssen elemeniert werden.
similarMovies=table.corrwith(table_sw)
similarMovies=similarMovies.dropna()
similarMovies=pd.DataFrame(similarMovies)
similarMovies=similarMovies.sort_values(by=0,ascending=False)

#Wir erstellen daher ein neues DataFrame, welches zu jedem Film die Anzahl speichert, wie oft dieser Film bewertet wurde
# und was die durchschnittliche Bewertung war. Das könnte später nützlich sein:
df1=pd.DataFrame(ratings.groupby('title')['rating'].count())
df2=pd.DataFrame(ratings.groupby('title')['rating'].mean())
df_merged=pd.merge(df1,df2,how='inner',left_on='title',right_on='title')
df_merged=df_merged.rename(columns={"rating_x": "Count", "rating_y": "Mean", 0:'Similarity'})



#Jetzt entfernen wir alle Filme, die von weniger als 100 Personen bewertet wurden, und schauen uns die übrig gebliebenen an:
df_100 = df_merged[df_merged['Count'] >100]
df_100=pd.merge(df_100,similarMovies,how='inner',left_on='title',right_on='title')
df_100=df_100.rename(columns={0:'Similarity'})
df_100=df_100.sort_values('Similarity', ascending = False)# - Sortierung der Werte auf(ascending=True) oder absteigend (ascending=False)
df_100.head(12)
# Jetzt macht die Modellierung Sinn!!