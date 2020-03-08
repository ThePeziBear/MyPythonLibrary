# used Functions - unique(), create dictionary with zip

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from sklearn.model_selection import train_test_split

df = pd.read_table('class_fruit_data_with_colors.txt')
df.head(10)

# create a mapping from fruit label value to fruit name to make results easier to interpret
key=df.fruit_label.unique()
value = df.fruit_name.unique()

lookup_fruit=dict(zip(key,value))

print(value)