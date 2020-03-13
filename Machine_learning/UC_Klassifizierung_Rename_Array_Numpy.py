#What is the class distribution? (i.e. how many instances of malignant (encoded 0) and how many benign (encoded 1)?)

#This function should return a Series named target of length 2 with integer values and index = ['malignant', 'benign']

def answer_two():

    cancerdf = answer_one() # sieh UC_KNN_Numpy_Pandas
    mal = np.where(cancer['target'] == 0) # Array aller Einträge  die 0 haben.
    ben = np.where(cancer['target'] == 1) # Array aller Einträge  die 1 haben.
    data = [np.size(mal), np.size(ben)] # Bildung Summe von 0 und 1 Einträgen als Anzahl
    index = ['malignant', 'benign'] # Erstellen eines Index maligant = 0 & benign = 1
    series = pd.Series(data,index=index) # Erstellen der Serie
    return series.rename('target') # Umbennen der Serienname

answer_two()


# alterantive Variante - Umwandlung Array in list

d=cancer['target'].tolist()
list0=[]
list1=[]

for i in d:
    if i == 1:
        list1.append(i)
    elif i ==0:
        list0.append(i)
    else:
        None

anzahl0=len(list0)
anzahl0
anzahl1=len(list1)
anzahl=[anzahl0, anzahl1]
index=('maligant','beinign')
Serie=pd.Series(anzahl, index)
Serie
