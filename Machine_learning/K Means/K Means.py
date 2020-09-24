## Methode zur Erzeugung von Daten

from numpy import random, array

# Erstelle zufällige Einkommen / Alter - Cluster für N personen in k Cluster
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = N/k
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = array(X)
    return X



## Modellierungsprozess

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float
import pandas as pd

data= pd.DataFrame(createClusteredData(100,5))

model = KMeans(n_clusters=5)

# Hier werden die Daten normalisiert. Das ist wichtig, damit die Zurodnung sauber funktioniert!
model = model.fit(scale(data))

# Ausgabe der Cluster
print(model.labels_)

# Anzeigen der Daten in einem Grafik
plt.figure(figsize=(8, 6))
plt.scatter(data[0], data[1], c=model.labels_.astype(float))
plt.show()