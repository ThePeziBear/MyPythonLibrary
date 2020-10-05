import seaborn as sns
import pandas as pd
import numpy as np

##Datasets

#Dataset für labeled Data
iris = sns.load_dataset('iris')
X = iris.drop('species',axis=1)
y = iris['species']

#Dataset für numeric Data
from sklearn.datasets import load_boston
boston = load_boston()
df = pd.DataFrame(boston['data'],columns = boston['feature_names'])
df['PRICE'] = boston['target']
X_n = df[['CRIM', 'ZN', 'INDUS','CHAS', 'NOX','RM', 'AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']]
y_n = df['PRICE']

# Training und Testdaten definieren
from sklearn.model_selection import train_test_split
X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_n, y_n, test_size=0.4, random_state=101)

# Erstellung und Training des Modells

## Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101) #Testsize (70%Training,30%Test), Random_state= Startwert für zufällige Datenauswahl



## Modelle:

# lineare Regression
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train_n,y_train_n)

predictions_linear_reg=lm.predict(X_test_n)


# logistic Regression
from sklearn.linear_model import LogisticRegression
log_model= LogisticRegression()
log_model.fit(X_train, y_train)
predictions_logistic_reg = log_model.predict(X_test)

#multivariante Regression

import statsmodels.api as sm
## Modellerstellung
X1 = sm.add_constant(X_n)
est = sm.OLS(y_n, X1).fit()


# Suport Vector Machine
from sklearn.svm import SVC
svc_model = SVC() #Instanzieren des Algorithmus
svc_model.fit(X_train,y_train) #Training
predictions_svm = svc_model.predict(X_test) # Vorhersage
            # Gridsearch - siehe Beispiel SVM
            # Die richtigen Parameter zu finden (wie C oder Gamma Werte) ist etwas knifflig.
            # Glücklicherweise können wir ein bisschen "faul" sein und eine Kombination verschiedener Varianten testen und sehen was am besten funktioniert.
            # Die Idee ein "Grid" an Parametern zu erstellen und einfach auszuprobieren wird "Gridsearch" genannt.
            # Da diese Methode recht üblich ist bietet SciKit Learn eine eingebaute Funktion namens GridSearchCV.
            # Dabei steht das CV für "Cross Validation". Und dies wiederum bedeutet, dass GridSearchCV ein Dictionary verwendet, das die Parameter beschreibt, die getestet werden sollen, und ein Modell, das es zu trainieren gilt


#Decision Tree
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()

dtree.fit(X_train,y_train)
predictions_trees = dtree.predict(X_test)

#Random Forrest
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10)
rfc.fit(X_train, y_train)
predictions_r_forest = rfc.predict(X_test)


## Auswertungen

#Classifaction Metriken
from sklearn.metrics import classification_report,confusion_matrix
matrix_svm= confusion_matrix(y_test,predictions_svm)
report_svm= classification_report(y_test,predictions_svm)

matrix_trees= confusion_matrix(y_test,predictions_trees)
report_trees= classification_report(y_test,predictions_trees)

matrix_r_forest= confusion_matrix(y_test,predictions_r_forest)
report_r_forest= classification_report(y_test,predictions_r_forest)

matrix_r_logisitc_reg= confusion_matrix(y_test,predictions_logistic_reg )
report_r_logistic_reg= classification_report(y_test,predictions_logistic_reg )


#numerische Metriken

# lineare Regression
from sklearn import metrics
MAE_linear_r=metrics.mean_absolute_error(y_test_n, predictions_linear_reg)
MSE_linear_r= metrics.mean_squared_error(y_test_n, predictions_linear_reg)
RMSE_linear_r= np.sqrt(metrics.mean_squared_error(y_test_n, predictions_linear_reg))

# multivariante Regression
metrik_multivariante_regression = est.summary()