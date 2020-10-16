#Dataset import

import pandas as pd
df1=pd.read_csv('./ml-100k/u.data',sep='\t',names=('user_id', 'movie_id', 'rating'),usecols=range(3))
df1


# Select Feature und Target Values
df1_mean=df1.groupby('movie_id')['rating'].mean()
df1=df1.groupby('movie_id').count()
df1['mean']=df1_mean.round(0)
df1.drop('user_id',axis=1,inplace=True)
df1.rename(columns={'rating':'size','mean':'target_rating'},inplace=True)

movieDict = {}
with open(r'./ml-100k/u.item', encoding="ISO-8859-1") as f:
    temp = ''
    genre=[]
    for line in f:
        fields = line.rstrip('\n').split('|')
        genres = fields[5:25]
        genres = [int(g) for g in genres]
        genre.append(genres)

genre = np.array(genre)

genre_sum = np.sum(genre * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], axis=1,
                   dtype=float) / 19

df1['genre'] = genre_sum

#Datamanipulation

#Eingrenzen der Daten
df1 = df1[df1['size'] > 90]
df1 = df1[df1['size'] < 220]

# Skalierung der Daten
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

df_x=pd.DataFrame(X)
plt.scatter(df_x[0],df_x[1])
