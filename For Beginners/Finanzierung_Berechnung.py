import pandas as pd
import numpy as np

invest = 300000
EK_Quote= 0.3
FK_Quote= 1 - EK_Quote

i = 0.015
T=20
EK = invest * EK_Quote
FK = invest * FK_Quote

list=[]
for e in range (1,20):
    tilgung = invest - (invest/20)
    tilgung2= tilgung- (invest/20)
    list.append(tilgung2)

print(list)
