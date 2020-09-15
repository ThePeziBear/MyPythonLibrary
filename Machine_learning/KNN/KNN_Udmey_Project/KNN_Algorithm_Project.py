import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

## Datenimport
df=pd.read_csv('Classified Data',index_col=0) #index_col definiert welche Spalte den Index darstellt

## Variablen Standardisieren
# Der KNN-Klassifizierer sagt die Klasse eines gegeben Testobjekts durch seine Nähe zu anderen Beobachtungen heraus.
# Deshalb ist die Skala der Variablen wichtig. Variablen auf einer großen Skala (z.B. Distanz zwischen Städten in Metern) würden
# deshalb einen größeren Einfluss auf die Klassifizerung haben als solche mit Kleiner Skala (z.B. Tag des Monats)

# Um dies zu berücksichtigen standardisieren wir nun zuerst unsere Daten.

from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1)) # Berechnet den Mittelwert & die Standardabweichung die für die Skalierung(scaler.trasnform) verwendet wird.
scaled_features=scaler.transform(df.drop('TARGET CLASS', axis =1)) #Die Daten werden an die berechneten Mittelwerte & std von fit angepasst.

df_feat = pd.DataFrame(scaled_features,columns=('WTT','PTI','EQW','SBI','LQE','QWG','FDJ','PJF','HQE','NXJ'))

## Train test Split

from sklearn.model_selection import train_test_split
X=scaled_features
y=df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


## KNN Modellierung

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1,algorithm='auto',metric='euclidean') # Auswahl der Paramater für das Modell: Anzahl Nearst neighbor, Algorithmus(auto,kd_tree etc) Metric(euclidean distance, manhattan etc)

knn.fit(X_train,y_train) #Anwendung des Modells auf Trainingsdaten

#Prognose und Auswertung nach Kennzahlen

prediction =knn.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,prediction))

print(classification_report(y_test,prediction))

## Den richtigen K-Wert finden
# Mit der Elbow-Methode kann man den optimalen K-Wert finden

def get_best_k(X_train,y_train,X_test,y_test):
    errorrate=[]
    for i in range(1,40):
        knn=KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train,y_train)
        pred=knn.predict(X_test)
        errorrate.append(np.mean(pred!=y_test))
    return errorrate

get_best_k(X_train,y_train,X_test,y_test)

k_values = get_best_k(X_train,y_train,X_test,y_test)

plt.figure(figsize=(12,8))
plt.plot(k_values,marker='o')

## Einsetzen des K-Values bei 21
knn = KNeighborsClassifier(n_neighbors=21)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('Mit K=21')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))