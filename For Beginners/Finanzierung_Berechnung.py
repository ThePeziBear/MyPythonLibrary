import pandas as pd
import numpy as np

list1 = []
list2 = []
n = 20
value = 182000
rate = 0.015
for i in range(n):
    result = value
    list1.append(result)

df1 = pd.DataFrame(list1)
df1.columns = ["I"]


for i in range(n):
    result = value/n
    list2.append(result)

df2 = pd.DataFrame(list2)
df2.columns = ["T"]

result = pd.concat([df1, df2], axis=1, sort=False)

df = pd.DataFrame(result)
print(df)

M = []
M = []
for i in range(n):
    result = 1 + i
    M.append(result)

df['M'] = M


df['R']=df['T']*df['M']

df['RS'] = df['I'] - df['R']

df['annual_i'] = df['RS'] * rate
