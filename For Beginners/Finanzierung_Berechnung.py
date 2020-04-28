import pandas as pd
import numpy as np

invest = 300000
EK_Quote= 0.3
FK_Quote= 1 - EK_Quote

i = 0.015
T=20
T_rate = invest/T
EK = invest * EK_Quote
FK = invest * FK_Quote



list1 = []
list2 = []
n = 20
value = 182000
rate = 0.015
for i in range(20):
    result = value
    list1.append(result)

df1 = pd.DataFrame(list1)
print (df1)


for i in range(20):
    result = value/n
    list2.append(result)

df2 = pd.DataFrame(list2)
print (df2)





# result = value * (1+rate) ** 20

# value = float(input("Enter initial value: "))
# rate = float(input("Enter the annual interest rate: "))
# time = float(input("Enter the time: "))
# result = invest_calc(value, rate)


#list1=[]
#list2=[]
#for z in range (1,20):
#    tilgung = int(invest) - int((invest/20))
#    list1.append(tilgung)



#print(list1)
