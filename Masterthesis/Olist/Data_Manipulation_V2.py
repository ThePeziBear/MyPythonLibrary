# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import all datasets
df_customers=pd.read_csv('olist_customers_dataset.csv')
df_geolocation=pd.read_csv('olist_geolocation_dataset.csv')
df_order_items=pd.read_csv('olist_order_items_dataset.csv')
df_order_pay=pd.read_csv('olist_order_payments_dataset.csv')
df_order_reviews=pd.read_csv('olist_order_reviews_dataset.csv')
df_orders=pd.read_csv('olist_orders_dataset.csv')
df_products=pd.read_csv('olist_products_dataset.csv')
df_sellers=pd.read_csv('olist_sellers_dataset.csv')
df_product_cat=pd.read_csv('product_category_name_translation.csv')


## Merge datasets for one big with all informations
df=pd.merge(df_orders,df_order_items,on='order_id', how='right')
df=df.merge(df_products, on='product_id')
df=df.merge(df_order_reviews,on='order_id')
df=df.merge(df_sellers,on='seller_id')
df=df.merge(df_customers,on='customer_id')
df = df.rename(columns={'price':'product_price','order_item_id':'quantity'})
df = df.drop(['review_id', 'review_creation_date','review_answer_timestamp','review_comment_title','review_comment_message','customer_id'], axis=1)

print(df.groupby(by='order_status').count()) #Take look at the distribution of order status

df = df[df['order_status'] == 'delivered'] # just delivered products are relevant for rating_review

## Creating Features for Dataset: Product avg Score, Product Price avg, Seller Score avg

#Create product score and product avg price
product_scored=df.groupby(by='product_id')['review_score'].mean()
product_avg_price=df.groupby(by='product_id')['product_price'].mean()
df_product_calc=pd.concat([product_scored,product_avg_price],axis=1)
df_product_calc=df_product_calc.reset_index()
df_product_calc=df_product_calc.rename(columns={'review_score':'score_product_avg','product_price':'product_price_avg'})

#Create Seller Score
seller_scored=df.groupby(by='seller_id')['review_score'].mean()
df_seller_scored=pd.DataFrame(data=seller_scored)
df_seller_scored=df_seller_scored.reset_index()
df_seller_scored=df_seller_scored.rename(columns={'review_score':'seller_score_avg'})

#Merge new Features to major dataset
df=df.merge(df_product_calc, on='product_id')
df=df.merge(df_seller_scored, on='seller_id')

#Show all nan_values
#sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='terrain')

dfnull=df[df.product_name_lenght=='nan']


## Dimensions Reduction - PCA and Feature Selection


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X=df[['product_price','freight_value','product_name_lenght','product_description_lenght','product_photos_qty',
      'product_weight_g','product_length_cm','product_height_cm','product_width_cm','score_product_avg','product_price_avg','seller_score_avg','review_score']]
X=X.dropna()
y = X['review_score']
X=X.drop(['review_score'],axis=1)
X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
df_feat=pd.DataFrame(X_new)
df_feat['reviews'] = y
df_feat=df_feat.rename(columns= {0:'feat1',1:'feat2'})

#sns.lmplot(x='feat1',y='feat2',data=df_feat,hue='reviews',palette='cubehelix',#hue: Trennung von kategorischen Parameter
#            #markers=['o','v'], #Veränderung der Symbole
#            scatter_kws={'s':10}) #scatter_kws: Definition von der Göße der Symbole


## Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_feat[['feat1','feat2']], y, test_size=0.30, random_state=101) #Testsize (70%Training,30%Test), Random_state= Startwert für zufällige Datenauswahl


#Decision Tree
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()

dtree.fit(X_train,y_train)
predictions_trees = dtree.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
matrix_trees= confusion_matrix(y_test,predictions_trees)
report_trees= classification_report(y_test,predictions_trees)

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


#KNN
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=4,algorithm='auto',metric='euclidean') # Auswahl der Paramater für das Modell: Anzahl Nearst neighbor, Algorithmus(auto,kd_tree etc) Metric(euclidean distance, manhattan etc)
knn.fit(X_train,y_train)
predictions_knn =knn.predict(X_test)


## Auswertungen

#Classifaction Metriken
from sklearn.metrics import classification_report,confusion_matrix
matrix_svm= confusion_matrix(y_test,predictions_svm)
report_svm= classification_report(y_test,predictions_svm)

matrix_trees= confusion_matrix(y_test,predictions_trees)
report_trees= classification_report(y_test,predictions_trees)

matrix_r_forest= confusion_matrix(y_test,predictions_r_forest)
report_r_forest= classification_report(y_test,predictions_r_forest)


matrix_knn= confusion_matrix(y_test,predictions_knn)
report_knn= classification_report(y_test,predictions_knn)
