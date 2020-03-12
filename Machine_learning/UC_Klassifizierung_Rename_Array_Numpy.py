#What is the class distribution? (i.e. how many instances of malignant (encoded 0) and how many benign (encoded 1)?)

#This function should return a Series named target of length 2 with integer values and index = ['malignant', 'benign']

def answer_two():
    cancerdf = answer_one()
    mal = np.where(cancer['target'] == 0)
    ben = np.where(cancer['target'] == 1)
    data = [np.size(mal), np.size(ben)]
    index = ['malignant', 'benign']
    series = pd.Series(data,index=index)
    return series.rename('target')

answer_two()

