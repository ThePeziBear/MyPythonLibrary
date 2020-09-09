import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_boston
boston = load_boston()
boston['data'].shape
print(boston.DESCR)

## Import Daten
df = pd.DataFrame(boston['data'],columns = boston['feature_names'])
df['PRICE'] = boston['target']


## Training eines linearen Regressionsmodell
# Das Ziel mit dem Regressionsmodell ist die Vorhersage des Preises.

# Daher wird ein X-Array (Features) und ein Y-Array (Zielvariable) gebildet
X = df[['CRIM', 'ZN', 'INDUS','CHAS', 'NOX','RM', 'AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']]
y = df['PRICE']

# Training und Testdaten definieren
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# Erstellung und Training des Modells

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

## Modellbewertung
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient']) # Koeffizient gibt an, wie sich die Veränderung von 1 Einheit z.B. Number of Bedrooms sich auf den Preis auswirkt.
# Es ist zum Beispiel der Koeffizient, das wenn dass Alter des Hauses um 1 Jahr steigt sich der Preis um 164883.282027 USD, nicht logisch. Das Datenset ist ein manilpuliertes

## Prediction des Modells

predictions=lm.predict(X_test)
reg=plt.scatter(y_test,predictions) # Die Punkte zeigen eine logische Verteilung
plt.show()

##Residuen Diagramm - Das Diagramm sollte eine Normalverteilung aufweisen.
#Existiert in den Residuen ein Muster (sind sie also nicht normal verteilt), so kann man es meistens schnell in dem Residuendiagramm sehen.
#Dies kann man sich auch mit einer einfachen Analogie vorstellen: wenn man Roulette spielt, sollte man nicht in der Lage sein, die Zahlen vorherzusagen (auch wenn man das gerne möchte).
#Man kann sich aber die gespielten Zahlen anschauen, um zu sehen, ob ein Muster dahin vorhanden ist.
#Diese Analogie kann man auch auf Regressionsmodelle übertragen: man sollte nicht in der Lage sein, auch nur ein einziges Residum vorherzusagen.
# Wenn in den Residuen ein Muster vorhanden ist, das es uns erlaubt, sie vorherzusagen, deutet dies darauf hin, dass das Regressionsmodell einen systematischen Fehler hat.

histo= sns.distplot((y_test-predictions),bins=50)
plt.show()

## Auswertmetriken

#Mean Absolute Error (MAE) ist der Durchschnitt des absoluten Werts der Fehler
#MAE ist am leichtesten zu verstehen, da sie den durchschnittlichen Error angibt

# Mean Squared Error (MSE) ist der Durchschnitt der quadrierten Fehlers (MAE)
# MSE ist verbreiteter, da MSE die größeren Errors "bestraft", was in der realen Welt nützlich ist.
# Eine geringe mittlere quadratische Abweichung bedeutet im klassischen Fall, dass gleichzeitig Verzerrung und Varianz des Schätzers klein sind.
# Man befindet sich mit dem Schätzer also im Mittel in der Nähe des zu schätzenden Funktionals (geringere Verzerrung) und weiß gleichzeitig,
# dass die Schätzwerte wenig streuen (geringe Varianz) und mit großer Wahrscheinlichkeit auch in der Nähe ihres Erwartungswerts liegen.
# Mit dem MSE ist es daher möglich, Schätzverfahren miteinander zu vergleichen.
#Viele Algorithmen verwenden MSE, da es schneller zu berechnen und einfacher zu manipulieren ist als RMSE.
# Es wird jedoch nicht auf den ursprünglichen Fehler skaliert (da der Fehler quadriert wird), was zu einem KPI führt, den wir nicht mit der ursprünglichen Nachfrageskala in Beziehung setzen können.
# Daher ist es ratsamer das RSME zu verwenden.


#Root Mean Squared Error(RSME) ist die Quadratwurzel des Durchschnitts der quardrierten Fehlers (MSE)
#Der RMSE sagt aus wie gut eine Funktion(skurve) an die Daten angepasst ist. Er sagt aus um wie viel im Durchschnitt die Schätzung von der Messung abweicht.
# Der RMSE ist immer im Zusammenhang mit den Daten selbst zu betrachten.

#WICHTIG: Vergleiche niemals Apfel mit Orangen, dh vergleiche niemals verschiedene Metriken miteinander.
# Vergleiche beispielsweise keine MSE-Werte mit MAE oder anderen. Sie sind anders.

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

#r2: Das R² gibt an, wie gut die unabhängige(n) Variable(n) geeignet sind, die Varianz der abhängigen zu erklären.
# Die Varianz ist ein Streuungsmaß, welches die Verteilung von Werten um den Mittelwert kennzeichnet. Sie ist das Quadrat der Standardabweichung.
# Berechnet wird die Varianz, indem die Summe der quadrierten Abweichungen aller Messwerte vom arithmetischen Mittel durch die Anzahl der Messwerte dividiert wird.
# Das R² liegt immer zwischen 0% (unbrauchbares Modell) und 100% (perfekte Modellanpassung). Zu beachten ist, dass das R² ein Gütemaß zum Beschreiben eines linearen Zusammenhangs darstellt.
from sklearn.metrics import r2_score
print('r2:',  r2_score(y_test, results))
