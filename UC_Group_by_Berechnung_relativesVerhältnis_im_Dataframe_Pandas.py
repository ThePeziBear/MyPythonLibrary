import pandas as pd
import numpy as np

df= pd.read_csv('Occupation_occupation.table', sep='|', index_col = 'user_id')
# variante anstelle index_col --> df = df.reset_index() --> df = df.set_index()
df.head()

df['gender_m'] = df['gender'] == 'M'
df['gender_m']=df['gender_m'].astype(int)

occ= df.groupby('occupation')['gender'].count()
occ_m= df.groupby('occupation')['gender_m'].sum()/occ
result = occ_m.sort_values(ascending = False)


# Variante mit Lambda
users = df

users['gender_n']=users['gender'].apply(lambda x: 1 if x== 'M' else 0) # gleicher Output wie zeile 8 & 9
r= users.groupby('occupation').gender_n.sum()/users.occupation.value_counts()
print(r.sort_values(ascending = False))