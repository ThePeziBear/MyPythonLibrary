## Dataset import

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1=pd.read_csv('./ml-100k/u.data',sep='\t',names=('user_id', 'movie_id', 'rating'),usecols=range(3))
df1


## Select Feature und Target Values
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

##Datamanipulation

#Eingrenzen der Daten
df1 = df1[df1['size'] > 90]
df1 = df1[df1['size'] < 220]

# Daten in Features und Targets defieren.
X=df1.iloc[:, 0:2].values
y=df1['target_rating'].values

# Skalierung der Daten
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

df_x=pd.DataFrame(X)
plt.scatter(df_x[0],df_x[1])

# Splitting des Datensets in Training set and Test set.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


## Modellierung
# Berechnung des besten K Values
def get_best_k(X_train,y_train,X_test,y_test):
    errorrate=[]
    for i in range(1,60):
        knn=KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train,y_train)
        pred=knn.predict(X_test)
        errorrate.append(np.mean(pred!=y_test))
    return errorrate

get_best_k(X_train,y_train,X_test,y_test)

k_values = get_best_k(X_train,y_train,X_test,y_test)

plt.figure(figsize=(12,8))
plt.plot(k_values,marker='o')


# Fitting classifier für Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 18)
classifier.fit(X_train, y_train)

# Predicting the Test set results
pred = classifier.predict(X_test)


## Auswertung der Metriken
from sklearn.metrics import classification_report,confusion_matrix
matrix= confusion_matrix(y_test,pred)
print(matrix)
report= classification_report(y_test,pred)
print(report)
