#used Methods: groupby(), sum(), unique()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Impfung_Dataframe.xlsx")
df.head()

df = df[['Impfung', 'Jahr','Anzahl']]
df.head()

group_Anzahl = df.groupby('Jahr')['Anzahl'].sum()
Jahre = df['Jahr'].unique()
plt.bar(Jahre,group_Anzahl)

dictionary_recommended = {'Hepatitis A+B' : 'recommended',
             'Hepatitis A' : 'recommended',
             'Hepatitis B' : 'recommended',
             'Grippe' : 'recommended',
             'FSME' : 'recommended',
             }

df['recommended'] = df['Impfung'].map(dictionary_recommended)

df2 = df[df['recommended'] == 'recommended']
group = df2.groupby('Jahr')['Anzahl'].sum()

Jahre = df['Jahr'].unique()

plt.bar(Jahre,group)

dictionary_kids = {'Masern-Mumps-Roeteln' : 'kids',
                   'Hib (Haemophilus influenzae b)' : 'kids',
                   'Diphtherie-Tetanus-Keuchhusten' : 'kids',
                   'Kinderlaehmung (Poliomyelitis)' : 'kids',
                   'Hepatitis B' : 'kids',
                   'Rotaviren' : 'kids',
                   'Pneumokokken' : 'kids',
                   }

df['kids'] = df['Impfung'].map(dictionary_kids)

df2 = df[df['kids'] == 'kids']
group = df2.groupby('Jahr')['Anzahl'].sum()

Jahre = df['Jahr'].unique()

plt.bar(Jahre,group)
plt.show