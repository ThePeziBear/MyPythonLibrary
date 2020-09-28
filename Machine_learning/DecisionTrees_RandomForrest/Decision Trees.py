import numpy as np
import pandas as pd
from sklearn import tree

input_file = "BisherigeEinstellungen.csv"
df = pd.read_csv(input_file, header = 0, sep = ";")
df.head()

d = {'J': 1, 'N': 0}
df['Hat Job bekommen?'] = df['Hat Job bekommen?'].map(d)
df['Aktuell angestellt?'] = df['Aktuell angestellt?'].map(d)
df['Elite-Uni'] = df['Elite-Uni'].map(d)
df['Hat Praktikum gemacht?'] = df['Hat Praktikum gemacht?'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Abschluss'] = df['Abschluss'].map(d)
df.head()

features = list(df.columns[:6])
features

y = df["Hat Job bekommen?"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

from IPython.display import Image
from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=features)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, y)

# Jemand hat 10 Jahre Job-Erfahrung, und aktuell einen Job.
# Wird er bei uns anfangen?
print(clf.predict([[10, 1, 4, 0, 0, 0]]))

# Jemand hat 10 Jahre Job-Erfahrung, und aktuell keinen Job.
# Wird er bei uns anfangen?
print(clf.predict([[10, 0, 4, 0, 0, 0]]))
