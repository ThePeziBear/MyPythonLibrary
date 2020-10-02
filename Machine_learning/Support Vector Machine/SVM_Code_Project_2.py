import seaborn as sns
iris = sns.load_dataset('iris')
X = iris.drop('species',axis=1)
y = iris['species']

## Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)#, random_state=101)


## Suport Vector Machine
from sklearn.svm import SVC
svc_model = SVC(C=1, kernel='linear') #Instanzieren des Algorithmus;
# C (Soft Margin) gibt die Toleranz der missklassifizierten Werte an. Je kleiner desto größer die Toleranz. default-value ist 1
# Das C verhält sich wie ein Regulierungsparameter in dem SVM.
# Kernel kann linear, poly, rbf, sigmoid - siehe weiter: https://scikit-learn.org/stable/modules/svm.html#svm-kernels

# Gamma definiert, wie viel Einfluss ein einzelnes Trainingsbeispiel hat.
# Je größer gamma ist, desto näher müssen andere Beispiele betroffen sein.
# Gamma ist ein freier Paramater von den gaußischen Radialbasisfunktion. Ein kleines Gamma bedeutet eine große Varianz --> SVM keine weitgestreuten Einfluss hat.
# Ein großes Gamma führt zu einer hohen Bias und zu einer niedrigen Varianz. Ein niedriges Gamma führt zu einem niedrigen Bias und hohen Varianz.
# siehe weiteres: https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html


svc_model.fit(X_train,y_train) #Training
predictions = svc_model.predict(X_test) # Vorhersage


## Auswertung ohne Gridsearch
from sklearn.metrics import classification_report,confusion_matrix
c_matrix= confusion_matrix(y_test,predictions)
c_report= classification_report(y_test,predictions)

#Was ist Gridsearch?
#Die richtigen Parameter zu finden (wie C oder Gamma Werte) ist etwas knifflig.
# Glücklicherweise können wir ein bisschen "faul" sein und eine Kombination verschiedener Varianten testen und sehen was am besten funktioniert.
# Die Idee ein "Grid" an Parametern zu erstellen und einfach auszuprobieren wird "Gridsearch" genannt.
#Da diese Methode recht üblich ist bietet SciKit Learn eine eingebaute Funktion namens GridSearchCV.
# Dabei steht das CV für "Cross Validation".
# Und dies wiederum bedeutet, dass GridSearchCV ein Dictionary verwendet, das die Parameter beschreibt, die getestet werden sollen, und ein Modell, das es zu trainieren gilt

## Gridsearch von Sklearn:

# Auswahl von verschiedenen Parametern für C und Gamma & die Kernel Funktion
param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}

from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)
# Estimator = SVC() - Angabe für das Modell
# param_grid - gibt die Prameter zum durchtesten der Parameter
# Refit = True - Beim Suchen der besten Parameter soll der Wert immer auf True sein.
# verbose= gibt die Anzahl der Zwischenschritte wider


# Modell mit den neuen C und Gamme werten neu trainieren
grid.fit(X_train,y_train)

# Den besten Parameter erhalten wir durch
print(grid.best_params_)

#Die besten parameter geben sich dann im Modell wieder.
print(grid.best_estimator_)

# Prediction des Modells mit gridsearch
grid_predictions = grid.predict(X_test)

# Auswertung des Modells mit gridsearch
c_matrix_cv= confusion_matrix(y_test,grid_predictions)
c_report_cv= classification_report(y_test,grid_predictions)