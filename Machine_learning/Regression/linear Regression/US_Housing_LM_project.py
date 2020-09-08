import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Import Daten
USAhousing = pd.read_csv('USA_Housing.csv')

## Übersicht des Datensets
head= USAhousing.head()
info= USAhousing.info()
describe= USAhousing.describe()

## Verteilung der Daten mit Seaborn Grafiken
sns.pairplot(USAhousing)
plt.show()

sns.distplot(USAhousing['Price'])
plt.show()

sns.heatmap(USAhousing.corr())
plt.show()

## Training eines linearen Regressionsmodell
# Das Ziel mit dem Regressionsmodell ist die Vorhersage des Preises.

# Daher wird ein X-Array (Features) und ein Y-Array (Zielvariable) gebildet
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

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
plt.scatter(y_test,predictions) # Die Punkte zeigen eine logische Verteilung


## Auswertmetriken

#Mean Absolute Error (MAE) ist der Durchschnitt des absoluten Werts der Fehler
#MAE ist am leichtesten zu verstehen, da sie den durchschnittlichen Error angibt

# Mean Squared Error (MSE) ist der Durchschnitt der quadrierten Fehlers (MAE)
# MSE ist verbreiteter, da MSE die größeren Errors "bestraft", was in der realen Welt nützlich ist.
# Eine geringe mittlere quadratische Abweichung bedeutet im klassischen Fall, dass gleichzeitig Verzerrung und Varianz des Schätzers klein sind.
# Man befindet sich mit dem Schätzer also im Mittel in der Nähe des zu schätzenden Funktionals (geringere Verzerrung) und weiß gleichzeitig,
# dass die Schätzwerte wenig streuen (geringe Varianz) und mit großer Wahrscheinlichkeit auch in der Nähe ihres Erwartungswerts liegen.
# Mit dem MSE ist es daher möglich, Schätzverfahren miteinander zu vergleichen.

#Root Mean Squared Error(RSME) ist die Quadratwurzel des Durchschnitts der quardrierten Fehlers (MSE)
#Der RMSE sagt aus wie gut eine Funktion(skurve) an die Daten angepasst ist. Er sagt aus um wie viel im Durchschnitt die Schätzung von der Messung abweicht.
# Der RMSE ist immer im Zusammenhang mit den Daten selbst zu betrachten. Es sind keine generellen Aussagen über die Höhe des RMSE-Wertes zu treffen.

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))