import pandas as pd
import numpy as np

df= pd.read_csv('Occupation_occupation.table', sep='|', index_col = 'user_id')
#occupation_data= occupation_data.set_index('user_id')
df.head()


df['gender_m'] = df['gender'] == 'M'
df['gender_m']=df['gender_m'].astype(int)
#df['gender'] = df['gender'].astype(int)

r= df.groupby('occupation').gender_m.sum()/df.occupation.value_counts()
r.sort_values(ascending = False)

#occ= df.groupby('occupation')(['gender_m']==1).count()

occ= df.groupby('occupation')['gender'].count()
occ_m= df.groupby('occupation')['gender_m'].sum()/occ
occ_m.sort_values(ascending = False)