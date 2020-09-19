from pylab import *
import numpy as np

#Ertellung eines Datensets
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

#Erstellung einer Polynomfunktion 8 Grades
p8 = np.poly1d(np.polyfit(x, y, 8))

import matplotlib.pyplot as plt

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p8(xp), c='r')
plt.show()

# Berechnen des r2
from sklearn.metrics import r2_score

r2 = r2_score(y, p4(x))

print(r2)
