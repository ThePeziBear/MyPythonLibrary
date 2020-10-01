import seaborn as sns
iris = sns.load_dataset('iris')
X = iris.drop('species',axis=1)
y = iris['species']

## Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# Suport Vector Machine
from sklearn.svm import SVC
svc_model = SVC() #Instanzieren des Algorithmus
svc_model.fit(X_train,y_train) #Training
predictions = svc_model.predict(X_test) # Vorhersage


## Auswertung ohne Gridsearch
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))