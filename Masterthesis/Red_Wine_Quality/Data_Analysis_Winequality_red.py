import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Import Data
df=pd.read_csv('winequality-red.csv',sep=',')

df_feat=df.drop(columns=['quality'])

#Data Manipulation
df_target=df['quality']


X=df_feat
y=df_target

X_array=X.to_numpy()

#Dimensionsreduction with PCA

from sklearn.decomposition import PCA
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)
varianz_pca= pca.explained_variance_ratio_ #Erklärt wieviel Varianz aufgrund der Reduktion erhalten wurde
print(X_pca.shape) #Zeigt dass die Daten auf 6Dimensionen reduziert wurden.

df_com=pd.DataFrame(X_pca,columns=['f1','f2'])
df_com['quality']=y
X=df_com[['f1','f2']]
# Visualizing DATA
categories = np.unique(df_com['quality'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]

plt.figure(figsize=(6, 4), dpi= 80, facecolor='w', edgecolor='b')

for i, quality in enumerate(categories):
    plt.scatter('f1', 'f2',
                data=df_com.loc[df_com.quality==quality, :],
                s=5, c=colors[i], label=str(quality))

plt.gca().set(xlabel='f1', ylabel='f2')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)
plt.show()


# Training und Testdaten definieren
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


# Suport Vector Machine
from sklearn.svm import SVC
svc_model = SVC() #Instanzieren des Algorithmus
svc_model.fit(X_train,y_train) #Training
predictions_svm = svc_model.predict(X_test) # Vorhersage

#Classifaction Metriken SVM
from sklearn.metrics import classification_report,confusion_matrix
matrix_svm= confusion_matrix(y_test,predictions_svm)
report_svm= classification_report(y_test,predictions_svm)


#KNN
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=29,algorithm='auto',metric='euclidean') # Auswahl der Paramater für das Modell: Anzahl Nearst neighbor, Algorithmus(auto,kd_tree etc) Metric(euclidean distance, manhattan etc)
knn.fit(X_train,y_train)
predictions_knn =knn.predict(X_test)

#Classifaction Metriken SVM
matrix_knn= confusion_matrix(y_test,predictions_knn)
report_knn= classification_report(y_test,predictions_knn)



