import seaborn as sns
iris = sns.load_dataset('iris')
X = iris.drop('species',axis=1)
y = iris['species']

## Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# Suport Vector Machine
from sklearn.svm import SVC
svc_model = SVC(C=0.5, kernel='linear') #Instanzieren des Algorithmus;
# C gibt die Toleranz der missklassifizierten Werte an. Je kleiner desto größer die Toleranz aus. default-value ist 1
# Kernel kann linear, poly, rbf, sigmoid - siehe weiter: https://scikit-learn.org/stable/modules/svm.html#svm-kernels

# Gamma definiert, wie viel Einfluss ein einzelnes Trainingsbeispiel hat.
# Je größer gamma ist, desto näher müssen andere Beispiele betroffen sein.


svc_model.fit(X_train,y_train) #Training
predictions = svc_model.predict(X_test) # Vorhersage


## Auswertung ohne Gridsearch
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

#Was ist Gridsearch?
#Die richtigen Parameter zu finden (wie C oder Gamma Werte) ist etwas knifflig.
# Glücklicherweise können wir ein bisschen "faul" sein und eine Kombination verschiedener Varianten testen und sehen was am besten funktioniert.
# Die Idee ein "Grid" an Parametern zu erstellen und einfach auszuprobieren wird "Gridsearch" genannt.
#Da diese Methode recht üblich ist bietet SciKit Learn eine eingebaute Funktion namens GridSearchCV.
# Dabei steht das CV für "Cross Validation".
# Und dies wiederum bedeutet, dass GridSearchCV ein Dictionary verwendet, das die Parameter beschreibt, die getestet werden sollen, und ein Modell, das es zu trainieren gilt

# Der