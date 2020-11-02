import pandas as pd

df_titles= pd.read_csv('movie_titles.csv',error_bad_lines=False,sep=',')
import pandas as pd

df_titles= pd.read_csv('movie_titles.csv', names = ['id', 'year', 'title'],error_bad_lines=False, header=None, encoding="latin1",warn_bad_lines=False)

df= pd.read_csv('./netflix/combined_data_1.txt',names = ['Cust_Id', 'Rating'], usecols = [0,1])

import numpy as np

df_nan = pd.DataFrame(pd.isnull(df.Rating))
df_nan = df_nan[df_nan['Rating'] == True]
df_nan = df_nan.reset_index()

movie_np = []
movie_id = 1

for i,j in zip(df_nan['index'][1:],df_nan['index'][:-1]):
    # numpy approach
    temp = np.full((1,i-j-1), movie_id)
    movie_np = np.append(movie_np, temp)
    movie_id += 1

# Account for last record and corresponding length
# numpy approach
last_record = np.full((1,len(df) - df_nan.iloc[-1, 0] - 1),movie_id)
movie_np = np.append(movie_np, last_record)


asdf


