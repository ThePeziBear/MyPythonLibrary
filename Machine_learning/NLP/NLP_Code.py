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

##Vektorisierung

#Aktuell liegen uns die Nachrichten als eine Listen von Tokens (auch als "Lemmas" bekannt) vor. Wir müssen jetzt jede dieser Nachrichten in einen Vektor umwandeln, mit dem SciKit Learn's Algorithmus arbeiten kann.

#Wir werden dazu die folgenden drei Schritte nach dem bag-of-words (bow) Modell durchführen:

#1.Zähle wie häufig ein Wort in jeder Nachricht vorkommt (Term Frequency)
#2.Gewichte die Anzahl, so dass häufige Wörter ein niedrigeres Gewicht erhalten (Inverse Document Frequency)
#3.Normalisiere den Vektor in Einheitslänge, um von der Länge des Originaltexts zu abstrahieren
# Literatur für vertiefendes Wissen: Stemming - https://de.wikipedia.org/wiki/Stemming; Part of Speech - http://www.nltk.org/book/ch05.html
# Literatur für fotgeschrittene Methoden zur Normalisierung: http://www.nltk.org/book/

#Da es so viele Nachrichten gibt können wir häufig die Anzahl 0 erwarten.
# Deshalb wird SciKit Learn eine Sparse Matrix ausgeben. siehe: https://de.wikipedia.org/wiki/D%C3%BCnnbesetzte_Matrix

from sklearn.feature_extraction.text import CountVectorizer

BagOfWords_transformer = CountVectorizer(analyzer=text_process).fit(messages['message']) # Es wird die Methode text_process zum cleanen des Datasets genommen
number_words= len(BagOfWords_transformer.vocabulary_) #wichtig ist das _ bei vocabulary_ damit das ganze Wörterverzeichnis genommen wird

##Plausicheck für transformer & Überprüfung Sparsity

message_test_4= messages['message'][3]

BagOfWords_test_4=BagOfWords_transformer.transform([message_test_4])
print(BagOfWords_test_4)
print(BagOfWords_transformer.get_feature_names()[4068])
    # Es zeigt dass die Nummer 4068 das "U" ist und 2 Mal vorkommt - check plausibel

BagOfWords_messages = BagOfWords_transformer.transform(messages['message'])

sparsity = (100.0 * BagOfWords_messages.nnz / (BagOfWords_messages.shape[0] * BagOfWords_messages.shape[1]))
    #Gleichung: NNZ(Number of NON Zerovalues) / shape[0] (Anzahl Messages) * shape[1] Anzahl Unique Wörter
    #Je niedriger der Wert von sparsity desto besser das DATASET



## TF-IDF Modellierung:

#Was ist TF-IDF?
#TF-IDF steht für term frequency-inverse document frequency. Diese Gewichtung wird häufig in der Informationsgewinnung und im Text Mining eingsetzt. Es ist ein statistisches Maß, das dazu dient auszuwerten, wie wichtig ein Wort in einem Dokument in einem Corpus ist. Die Wichtigkeit steigt proportional zur Anzahl der Erscheinungen des Worts im Dokument doch wird ausgeglichen durch die Häufigkeit des Worts im gesamten Corpus. Varianten der tf-idf Gewichtung werden häufig als wichtiges Tool von Suchmachinen verwendet, um die Wichtigkeit eines Dokuments für eine Nutzerabfrage zu beurteilen.
#Eine der einfachsten Ranking-Funktionen wird berechnet, indem die tf-idf für jedes Wort in der Suchanfrage summiert werden. Darüber hinaus gibt es deutlich komplexere Ranking-Funktionen basierend auf diesem einfachen Modell.

#Typischerweise setzt sich das tf-idf Gewicht aus zwei Teilen zusammen:
#TF: Term Frequency - wie häufig erscheint ein Wort in einem Dokument geteilt durch die Anzahl aller Wörter.
#IDF: Inverse Document Frequency - Logarithmus der Gesamtzahl an Dokumenten geteilt durch die Anzahl der Dokumente, die ein bestimmtes Wort enthalten.

#Beispiel:
#:Stelle dir ein Dokument vor, das 100 Wörter beinhaltet. Darin erscheint das Wort "Katze" drei mal.

#Die TF für "Katze" ist dann (3/100)=0.03.
#Stelle dir jetzt weiter vor, dass wir 10 Millionen Dokumente haben. In 1000 davon erscheint das Wort Katze. Dann wird die IDF durch log(10,000,000/1,000) = 4 berechnet.
#Dementsprechend berechnet sich das TF-IDF Gewicht als das Produkt dieser Zahlen: 0.03* * 4 = 0.12.

from sklearn.feature_extraction.text import TfidfTransformer #Import tfidf Modell von Sklearn

tfidf_trans = TfidfTransformer().fit(BagOfWords_messages) #Anwendung des Modells auf Daten

#Plausi-Check
tfidf4=tfidf_trans.transform(BagOfWords_test_4) #Anwendung des Modells auf SMS Message Nr4. als Plauscheck
word_ranking_test=(tfidf_trans.idf_[BagOfWords_transformer.vocabulary_['university']])



