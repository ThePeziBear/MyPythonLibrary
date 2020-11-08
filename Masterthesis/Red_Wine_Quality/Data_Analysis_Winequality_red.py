import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


df=pd.read_csv('winequality-red.csv',sep=',')

df_feat=df.drop(columns=['quality'])
print(df_feat)

df_target=df['quality']
df_top_wine=df[df['quality']>=5]
#sns.pairplot(df,hue='quality',palette='coolwarm')


X=df_feat
y=df_target

X1=sm.add_constant(X)
est=sm.OLS(y,X1).fit()
summary_stat=est.summary()

#plt.scatter(X,y)
#plt.scatter(df['volatile acidity'],df['fixed acidity'])

X_array=X.to_numpy()

from sklearn.decomposition import PCA
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)
varianz_pca= pca.explained_variance_ratio_ #Erklärt wieviel Varianz aufgrund der Reduktion erhalten wurde
print(X_pca.shape) #Zeigt dass die Daten auf 6Dimensionen reduziert wurden.

df_com=pd.DataFrame(X_pca,columns=['f1','f2'])
df_com['quality']=y
sns.stripplot(x='f1',y='f2',hue='quality',data=df_com)
