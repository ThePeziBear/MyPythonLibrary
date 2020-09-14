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



