import pandas as pd

# Lists for Dataframe
list1 = []
list2 = []
M = []

# parameter for calculation
n = 20
value = 182000
rate = 0.015

# creating arrays for DataFrame
for i in range(n):
    result = value
    list1.append(result)

df1 = pd.DataFrame(list1)
df1.columns = ["capital"]

for i in range(n):
    result = value/n
    list2.append(result)

df2 = pd.DataFrame(list2)
df2.columns = ["repayment"]

for i in range(n):
    result = 0 + i
    M.append(result)

#creating Dataframe
list_to_df = pd.concat([df1, df2], axis=1, sort=False)
df = pd.DataFrame(list_to_df)

# calculations and adding columns to dataframe
df['mulitplikator'] = M
df['refund/year']=df['repayment']*df['mulitplikator']
df['residual debt'] = df['capital'] - df['refund/year']
df['interest'] = df['residual debt'] * rate

interest_total= df['interest'].sum()
repayment_total= df['repayment'].sum()

payment_total = interest_total+repayment_total

interest_debt_capital = (payment_total/value)-1

#from tkinter import *
#root = Tk()
#theLabel= Label(root, text='Invest')
#theLabel.pack()
#root.mainloop()window = tkinter.Tk()
# to rename the title of the window
import tkinter
window = tkinter.Tk()
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Welcome to the Amazing Invest Calculator!").pack()
window.mainloop()