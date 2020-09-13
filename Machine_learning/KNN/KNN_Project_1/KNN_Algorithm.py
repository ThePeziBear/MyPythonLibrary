import matplotlib.pyplot as plt
import math

#house ownership

age_no = (23,37,52,25,20)
income_no=(50000,34000,30000,78000,100000)
age_yes=(48,28,35,32,40)
income_yes=(40000,95000,130000,105000,60000)

minage = 20
maxage = 52
minincome = 30000
maxincome = 130000

def rescale(value, minvalue, maxvalue):
    return ((float)(value - minvalue) / (float)(maxvalue - minvalue))


age_no_scaled = [rescale(_, minage, maxage) for _ in age_no]
age_yes_scaled = [rescale(_, minage, maxage) for _ in age_yes]
income_no_scaled = [rescale(_, minincome, maxincome) for _ in income_no]
income_yes_scaled = [rescale(_, minincome, maxincome) for _ in income_yes]

dataset = (age_no[0], income_no[0]), (age_no[1], income_no[1]), (age_no[2], income_no[2]), (age_no[3], income_no[3]), (
age_no[4], income_no[4]), (age_yes[0], income_yes[0]), (age_yes[1], income_yes[1]), (age_yes[2], income_yes[2]), (
          age_yes[3], income_yes[3]), (age_yes[4], income_yes[4])

dataset_scaled = (age_no_scaled[0], income_no_scaled[0]), (age_no_scaled[1], income_no_scaled[1]), (
age_no_scaled[2], income_no_scaled[2]), (age_no_scaled[3], income_no_scaled[3]), (
                 age_no_scaled[4], income_no_scaled[4]), (age_yes_scaled[0], income_yes_scaled[0]), (
                 age_yes_scaled[1], income_yes_scaled[1]), (age_yes_scaled[2], income_yes_scaled[2]), (
                 age_yes_scaled[3], income_yes_scaled[3]), (age_yes_scaled[4], income_yes_scaled[4])

dic = {}

for i in range(0, len(age_no_scaled)):
    dic[age_no_scaled[i], income_no_scaled[i]] = 'No'

for i in range(0, len(age_yes_scaled)):
    dic[age_yes_scaled[i], income_yes_scaled[i]] = 'Yes'

dic[(0.09375, 0.2)]

dic_non_scaled = {}

for i in range(0, len(age_no)):
    dic[age_no[i], income_no[i]] = 'No'

for i in range(0, len(age_yes)):
    dic[age_yes[i], income_yes[i]] = 'Yes'




def euclidean_distance(x,y):
    a, b = x
    c, d = y
    return math.sqrt((a-c)*(a-c)+(b-d)*(b-d))

def get_neighbors(data, new_one, k):
    distances = []
    for data in data:
        dist = euclidean_distance(new_one, data)
        distances.append((data, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

def predict(dataset, new_data,dic,k):
    neighbors = get_neighbors(dataset, new_data,k)
    output_values_list=[]
    for i in neighbors:
        output_values_list.append(dic[i])
    return output_values_list


# KNN scaled Data
new_age_scaled=((float)(50 - 20) / (float)(52 - 20))
new_income_scaled=((float)(80000 - 30000) / (float)(130000 - 30000))
new_data_scaled=(new_age_scaled,new_income_scaled)
dataset_scaled=[(age_no_scaled[0],income_no_scaled[0]),(age_no_scaled[1],income_no_scaled[1]),(age_no_scaled[2],income_no_scaled[2]),(age_no_scaled[3],income_no_scaled[3]),(age_no_scaled[4],income_no_scaled[4]),(age_yes_scaled[0],income_yes_scaled[0]),(age_yes_scaled[1],income_yes_scaled[1]),(age_yes_scaled[2],income_yes_scaled[2]),(age_yes_scaled[3],income_yes_scaled[3]),(age_yes_scaled[4],income_yes_scaled[4])]

Peters_decision_1=predict(dataset_scaled,new_data_scaled,dic,1)
print(str(Peters_decision_1) + (" - Peter will buy a House"))

plt.plot(age_no_scaled,income_no_scaled,color='blue',marker='o',linestyle='none')
plt.plot(age_yes_scaled,income_yes_scaled,color='red',marker='o',linestyle='none')
plt.plot(new_age_scaled,new_income_scaled,color='green',marker='x',linestyle='none')


plt.title("House Owners")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()


# KNN  non scaled Data

new_data=(50,80000)
get_neighbors(dataset,new_data,1)

Peters_decision_2=predict(dataset,new_data,dic,1)
print(str(Peters_decision_2) + (" - Peter will not buy a House"))

# Conlusio
#In der Prediction im Modell "KNN scaled Data" sind Age & Income gleich gewichtet. Die Daten im  Modell "KNN non scaled Data" ist aufgrund der ungleichen Werte (x=50, y=80000) wesentlich ungleicher gewichtet.
# Das Income hat eine extrem dominanten Einfluss auf den Vektor. Somit ergibt sich der Punkt (x=25,y=78000) als nearest Neighbor, wobei dieser falsch ist.