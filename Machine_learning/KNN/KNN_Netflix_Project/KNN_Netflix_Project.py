
import pandas as pd
import numpy as np

df1 = pd.read_csv('./ml-100k/u.data', sep='\t', names=('user_id', 'movie_id', 'rating'), usecols=range(3))
df1

df1_mean = df1.groupby('movie_id')['rating'].mean()
df1 = df1.groupby('movie_id').count()
df1['mean'] = df1_mean.round(0)
df1.drop('user_id', axis=1, inplace=True)
df1.rename(columns={'rating': 'size', 'mean': 'target_rating'}, inplace=True)
df1

movieDict = {}
with open(r'./ml-100k/u.item', encoding="ISO-8859-1") as f:
    temp = ''
    genre = []
    for line in f:
        fields = line.rstrip('\n').split('|')
        genres = fields[5:25]
        genres = [int(g) for g in genres]
        genre.append(genres)

genre = np.array(genre)

genre_sum = np.sum(genre * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], axis=1,
                   dtype=float) / 19

df1['genre'] = genre_sum
df1 = df1[['size', 'genre', 'target_rating']]
df1
dfx = df1[['size', 'genre']]  # ,'target_rating']]
dfx

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_norm_scaled = scaler.fit_transform(dfx)
df_x = pd.DataFrame(X_norm_scaled)
df_x.index += 1
df_x['target'] = df1['target_rating']
df_x

import plotly.express as px

fig = px.scatter(df_x, x=0, y=1, color='target')
fig.show()

df_x_new = df_x
# df_x_new = df_x_new[df_x_new[0]>0.1]
# df_x_new = df_x_new[df_x_new[0]<0.6]
# df_x_new = df_x_new[df_x_new[1]>0.16]
# df_x_new = df_x_new[df_x_new[1]<0.8]

df_x_new.info()

import plotly.express as px

fig = px.scatter(df_x_new, x=0, y=1, color='target')
fig.show()

X = df_x_new.iloc[:, 0:2].values
y = df_x_new['target'].values
X.shape

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=0)
X_test.shape

import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
def get_best_k(X_train, y_train, X_test, y_test):
    errorrate = []
    for i in range(1, 60):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred = knn.predict(X_test)
        errorrate.append(np.mean(pred != y_test))
    return errorrate


get_best_k(X_train, y_train, X_test, y_test)

k_values = get_best_k(X_train, y_train, X_test, y_test)

plt.figure(figsize=(12, 8))
plt.plot(k_values, marker='o')

# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=30)
classifier.fit(X_train, y_train)

#Predicting the Test set results
pred = classifier.predict(X_test)
pred.shape

from sklearn.metrics import classification_report, confusion_matrix

matrix = confusion_matrix(y_test, pred)
print(matrix)
report = classification_report(y_test, pred)
print(report)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

n_neighbors = 30
h=0.02

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA','#00AAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00','#9cdeff'])

# calculate min, max and limits for the Vizualation-Chart
x_min, x_max = X_test[:, 0].min() - 1, X_test[:, 0].max() + 1
y_min, y_max = X_test[:, 1].min() - 1, X_test[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))


# predict class using data and kNN classifier to get the borders
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(figsize=[10,6],dpi=750)
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Plot the Test Dataset points
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("3-Class classification (k = %i)" % (n_neighbors))
plt.show()