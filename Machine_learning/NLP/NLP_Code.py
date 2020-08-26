## Import Libraries
import nltk
nltk.download_shell()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Import Dataset
#Import Dataset

messages = pd.read_csv('Smsspamcollection/Smsspamcollection', sep='\t',
                       names=['label', 'message'])  # import der Daten ind Pandas zur explorativen Datenanalyse

## Datananalyse & Datamanipulation

#Datenanalyse 1
messages.describe() #statistische Standard Kennzahlen abrufen
messages.groupby('label').describe()

#Datenmanipulation
messages['length'] = messages['message'].apply(len) #Hinzufügen der Länge der Textnachrichten

#Datenanalyse 2
messages['length'].plot(bins=20, kind='hist')
messages.length.describe()
messages.hist(column='length',by='label',bins=50, figsize=(12,4))

#Datenmanipulation 2: Entfernung der Punktzeichen (nopunc) & Entfernung der Stopwords
import string
mess= 'Sample message! Notice: i we -,-,-,-'
nopunc=[char for char in mess if char not in string.punctuation] # Entfernung der Punktzeichen
nopunc = ''.join(nopunc)

#Entfernung der Stopwords - Stopwords sind sehr häufig wiederkehrende Wörter
#die jedoch nicht wesentlich für den Informationsgehalt des Textes ist.
from nltk.corpus import stopwords # Import der Library
blacklist = stopwords.words('english') # Auswahl der englischen Stopwords
clean_mess= [word for word in nopunc.split() if word.lower() not in blacklist] # lower(): ermöglicht Groß & Kleinschreibung zu berücksichtigen

#Erstellung einer Methode, die die Zeichensetzung, Stopwörter ersetzt und dann in eine Liste mit cleaned Text zurück gibt.
def text_process(mess): #Erstellung einer Funktion mit den oberen Variablen,damit wir es auf das DF anwenden können.
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in blacklist]

        # Folgendes macht die text_process Funktion
        #Nimmt einen String von Text und führt das folgende durch:
        #    1. Entferne alle Zeichensetzung
        #    2. Entferne alle Stoppwörter
        #    3. Gebe eine Liste des gesäuberten Texts zurück


## Überprüfung des 'cleaned text'
# Jetzt sind die Nachrichten "tokenized".
#Tokenization bezeichnet den Prozess der Kovertierung eines normalen Text Strings in eine Liste von Token (Wörter die wir tatsächlich verarbeiten wollen)

test_for_tokenize =messages['message'].head().apply(text_process)

