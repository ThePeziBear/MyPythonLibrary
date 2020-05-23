import matplotlib.pyplot as plt
import math

age_no = (23,37,52,25,20)
income_no=(50000,34000,30000,78000,100000)
age_yes=(48,28,35,32,40)
income_yes=(40000,95000,130000,105000,60000)

minage = 20
maxage = 52
minincome = 30000
maxincome = 130000


# Formel zum "rescaling" der Daten.
def rescale(value, minvalue, maxvalue):
    return ((float)(value - minvalue) / (float)(maxvalue - minvalue))

age_no_scaled = [rescale(_, minage, maxage) for _ in age_no]
age_no_scaled

age_yes_scaled = [rescale(_, minage, maxage) for _ in age_yes]
age_yes_scaled

income_no_scaled = [rescale(_, minincome, maxincome) for _ in income_no]
income_no_scaled

income_yes_scaled = [rescale(_, minincome, maxincome) for _ in income_yes]
income_yes_scaled



# Formel zur Berechnung der euklidischen Distanz
def euclidean_distance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance = distance + pow((instance1[x] - instance2[x]), length)
    return math.sqrt(distance)


#Rescaling des zu schätzendes Wertes
new_age_scaled=((float)(50 - 20) / (float)(52 - 20))
new_income_scaled=((float)(80000 - 30000) / (float)(130000 - 30000))

# Erstellen vom dataset
new_data_scaled=[new_age_scaled,new_income_scaled]

dataset_scaled=[(age_no_scaled[0],income_no_scaled[0]),(age_no_scaled[1],income_no_scaled[1],0),(age_no_scaled[2],income_no_scaled[2],0),(age_no_scaled[3],income_no_scaled[3],0),(age_no_scaled[4],income_no_scaled[4],0),(age_yes_scaled[0],income_yes_scaled[0],1),(age_yes_scaled[1],income_yes_scaled[1],1),(age_yes_scaled[2],income_yes_scaled[2],1),(age_yes_scaled[3],income_yes_scaled[3],1),(age_yes_scaled[4],income_yes_scaled[4],1)]

new_data_scaled


#Bestimmung des next Neigbors
def get_neighbors(dataset_scaled, new_data_scaled, k):
    distances = []
    for data in dataset_scaled:
        dist = euclidean_distance(new_data_scaled, data,2)
        distances.append((data, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

neighbors = get_neighbors(dataset_scaled, new_data_scaled, 1)
for neighbor in neighbors:
    print(neighbor)


# Predicition
def predict(dataset_scaled, new_data_scaled, k):
    neighbors = get_neighbors(dataset_scaled, new_data_scaled, k)
    output_values = [row[2] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count) # Für die Ausgabe nicht unbedingt erforderlich - ohne prediction bekommt man eine List
    return prediction

prediction = predict(dataset_scaled, new_data_scaled, 1)
print('Die Zahl '+str(prediction) + " bedeutet, dass sich Peter vermutlich ein Haus kaufen wird.")

plt.plot(age_no_scaled,income_no_scaled,color='blue',marker='o',linestyle='none')
plt.plot(age_yes_scaled,income_yes_scaled,color='red',marker='o',linestyle='none')
plt.plot(new_age_scaled,new_income_scaled,color='green',marker='x',linestyle='none')


plt.title("House Owners")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()
