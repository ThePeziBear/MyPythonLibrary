import numpy as np
import pandas as pd

# Methode zum Erstelle von zufälligen Einkommens / Alter - Daten für N Personen in k Clustern
def createClusteredData(N, k):
    pointsPerCluster = float(N)/k
    X = []
    y = []
    for i in range (k):
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        ageCentroid = np.random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y




from pylab import *

(X, y) = createClusteredData(100, 5)

df=pd.DataFrame(data=X)
df=df.rename(columns={0:'income', 1:'age'})

#Normalisieren der Werte
norm_income = [float(i)/max(df['income']) for i in df['income']]
norm_age = [float(i)/max(df['age']) for i in df['age']]

df_scaled=pd.DataFrame({'income_scaled':norm_income,'age_scaled':norm_age})
X=df_scaled.to_numpy()

plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
plt.show()

#Trainiere Modell
from sklearn import svm, datasets
C=1.0
svc=svm.SVC(kernel='linear',C=C).fit(X,y)

#Überprüfe Modelle-Güte
score= svc.score(df_scaled,y)

# Setze Punkte ein und lasse dir Prognose geben
print(svc.predict([[0.4,0.6]]))