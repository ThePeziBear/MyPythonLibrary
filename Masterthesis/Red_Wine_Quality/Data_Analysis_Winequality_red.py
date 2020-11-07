import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('winequality-red.csv',sep=',')

df_feat=df.drop(columns=['quality'])
print(df_feat)

df_target=df['quality']

sns.pairplot(df,hue='quality',palette='coolwarm')

plt.scatter(df['citric acid'],df['fixed acidity'])
sns.stripplot(x='volatile acidity',y='fixed acidity', data=df,hue='quality',palette='Set1')
