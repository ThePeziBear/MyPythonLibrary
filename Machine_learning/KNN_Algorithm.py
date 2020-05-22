# KNN - algorithm without library
import matplotlib.pyplot as plt
from collections import Counter
import math
import sys

age_no = (23,37,52,25,20)
income_no=(50000,34000,30000,78000,100000)
age_yes=(48,28,35,32,40)
income_yes=(40000,95000,130000,105000,60000)

age_no_scaled=(0.09375, 0.53125, 1.0, 0.15625, 0.0)
income_no_scaled=(0.2, 0.04, 0.0, 0.48, 0.7)
age_yes_scaled=(0.875, 0.25, 0.46875, 0.375, 0.625)
income_yes_scaled=(0.1, 0.65, 1.0, 0.75, 0.3)

dataset=[[23,50000,0],[37,34000,0],[52,30000,0],[25,78000,0],[20,100000,0],
         [48,40000,1],[28,95000,1],[35,130000,1],[32,105000,1],[40,60000,1]]

dataset_scaled=[[0.09375,0.2,0],[0.53125,0.04,0],[1.0,0.48,0],[0.15625,0.48,0],[0.0,0.7,0],
         [0.875,0.1,1],[0.25,0.65,1],[0.46875,1.0,1],[ 0.375, 0.75,1],[0.625,0.3,1]]


def euclidean_distance(x,y):
    distance = 0.0
    for i in range(len(x)):
        distance = (x[i] - y[i])**2
        return math.sqrt(distance)

def get_neighbors(train, test_row, num_neighbors):
    distances = []
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1]) # 2.Eintrag - erster Eintrag ähnelt natürlich
    neighbors = []
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

neighbors = get_neighbors(dataset_scaled, dataset_scaled[0], 1)
for neighbor in neighbors:
    print(neighbor)

new_data=[0.7, 0.8]

def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

prediction = predict_classification(dataset_scaled, new_data, 1)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))

plt.plot(age_no_scaled,income_no_scaled,color='blue',marker='o',linestyle='none')
plt.plot(age_yes_scaled,income_yes_scaled,color='red',marker='o',linestyle='none')

plt.title("House Owners")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()

