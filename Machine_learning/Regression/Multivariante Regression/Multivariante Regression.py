import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

## Daten laden
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

## Datenmanipulation

# Es werden die kategorischen Daten des Modells in ordinale numerische Daten umgewandelt
df['Model_ord'] = pd.Categorical(df.Model).codes

# Erstellen der Features für die Prognose
X = df[['Mileage', 'Model_ord', 'Doors']]
y = df[['Price']]

## Modellerstellung
X1 = sm.add_constant(X)
est = sm.OLS(y, X1).fit()

# Auswertung des Modells
summary = est.summary()