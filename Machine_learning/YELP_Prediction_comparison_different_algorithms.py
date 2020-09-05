import numpy as np
import pandas as pd

yelp = pd.read_csv('yelp.csv')

## Datenmanipulation
#Reduzierung DF für bessere Laufzeiten


#Entfernung von Punktzeichen - punctuation
import string
text= 'Sample message! Notice: i we -,-,-,-'
nopunc=[char for char in text if char not in string.punctuation] # Entfernung der Punktzeichen
nopunc = ''.join(nopunc)

#Entfernung von Stopwords
from nltk.corpus import stopwords # Import der Library
clean_text= [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

#Erstellung einer Methode für Datenmanipulation
def text_process(text): #Erstellung einer Funktion mit den oberen Variablen,damit wir es auf das DF anwenden können.
    nopunc = [char for char in text if char not in string.punctuation] #Entfernen aller Satzzeichen
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

        # Folgendes macht die text_process Funktion
        #Nimmt einen String von Text und führt das folgende durch:
        #    1. Entferne alle Zeichensetzung
        #    2. Entferne alle Stoppwörter
        #    3. Gebe eine Liste des gesäuberten Texts zurück

test_for_tokenize =df['text'].head().apply(text_process)
print(test_for_tokenize[0])

tokenized_text=df['text'].head().apply(text_process)

## Vektorisierung Text
#Vektorisierung der einzelnen Wörter im Text

from sklearn.feature_extraction.text import CountVectorizer
bow_transform=CountVectorizer(analyzer=text_process).fit(df['text'])

vektor_test=test_for_tokenize[2]
vektor_test