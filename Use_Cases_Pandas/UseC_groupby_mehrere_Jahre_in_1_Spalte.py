used Methods: groupby(), sum(), unique()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Impfung_Dataframe.xlsx")
df.head()

df = df[['Impfung', 'Jahr','Anzahl']]
df.head()

group_Anzahl = df.groupby('Jahr')['Anzahl'].sum()
Jahre = df['Jahr'].unique()
plt.bar(Jahre,group_Anzahl)

dictionary = {#'Hepatitis A+B' : 'aerztlich empfohlen',
             #'Hepatitis A' : 'aerztlich empfohlen',
             #'Hepatitis B' : 'aerztlich empfohlen',
             'Grippe' : 'aerztlich empfohlen',
             #'FSME' : 'aerztlich empfohlen',
             #'Meningokokken' : 'aerztlich empfohlen'
             #'Masern-Mumps-Roeteln' : 'aerztlich empfohlen'
             }

df['empfohlen'] = df['Impfung'].map(dictionary)

df2 = df[df['empfohlen'] == 'aerztlich empfohlen']
df2
group = df2.groupby('Jahr')['Anzahl'].sum()

Jahre = df['Jahr'].unique()

plt.bar(Jahre,group)