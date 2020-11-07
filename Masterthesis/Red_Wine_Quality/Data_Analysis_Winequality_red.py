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

#plt.scatter(df['citric acid'],df['fixed acidity'])
sns.stripplot(x='volatile acidity',y='fixed acidity', data=df_top_wine,hue='quality',palette='Set1')


