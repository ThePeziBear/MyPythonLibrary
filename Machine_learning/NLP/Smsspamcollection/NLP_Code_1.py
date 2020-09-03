## Import Libraries ##
import nltk
from sklearn.metrics import classification_report

nltk.download_shell()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Import Dataset ##
#Import Dataset

messages = pd.read_csv('Smsspamcollection', sep='\t',
                       names=['label', 'message'])  # import der Daten ind Pandas zur explorativen Datenanalyse

messages_1 = pd.read_csv('yelp.csv',names=['text','stars'])





## Datananalyse & Datamanipulation ##

##Datenanalyse 1
messages.describe() #statistische Standard Kennzahlen abrufen
messages.groupby('label').describe()

##Datenmanipulation
messages['length'] = messages['message'].apply(len) #Hinzufügen der Länge der Textnachrichten

##Datenanalyse 2
messages['length'].plot(bins=20, kind='hist')
messages.length.describe()
messages.hist(column='length',by='label',bins=50, figsize=(12,4))

##Datenmanipulation 2: Entfernung der Punktzeichen (nopunc) & Entfernung der Stopwords
import string
mess= 'Sample message! Notice: i we -,-,-,-'
nopunc=[char for char in mess if char not in string.punctuation] # Entfernung der Punktzeichen
nopunc = ''.join(nopunc)

#Entfernung der Stopwords - Stopwords sind sehr häufig wiederkehrende Wörter
#die jedoch nicht wesentlich für den Informationsgehalt des Textes ist.
from nltk.corpus import stopwords # Import der Library
blacklist = stopwords.words('english') # Auswahl der englischen Stopwords
clean_mess= [word for word in nopunc.split() if word.lower() not in blacklist] # lower(): ermöglicht Groß & Kleinschreibung zu berücksichtigen

##Methode: clean Stopwords, clean Zeichensetzung, return cleaned Text
#Erstellung einer Methode, die die Zeichensetzung, Stopwörter ersetzt und dann in eine Liste mit cleaned Text zurück gibt.
def text_process(mess): #Erstellung einer Funktion mit den oberen Variablen,damit wir es auf das DF anwenden können.
    nopunc = [char for char in mess if char not in string.punctuation] #Entfernen aller Satzzeichen
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in blacklist]

        # Folgendes macht die text_process Funktion
        #Nimmt einen String von Text und führt das folgende durch:
        #    1. Entferne alle Zeichensetzung
        #    2. Entferne alle Stoppwörter
        #    3. Gebe eine Liste des gesäuberten Texts zurück


# Überprüfung des 'cleaned text'
# Jetzt sind die Nachrichten "tokenized".
#Tokenization bezeichnet den Prozess der Kovertierung eines normalen Text Strings in eine Liste von Token (Wörter die wir tatsächlich verarbeiten wollen)
test_for_tokenize =messages['message'].head().apply(text_process)





##Vektorisierung##

#Aktuell liegen uns die Nachrichten als eine Listen von Tokens (auch als "Lemmas" bekannt) vor.
# Wir müssen jetzt jede dieser Nachrichten in einen Vektor umwandeln, mit man SciKit Learn's Algorithmus arbeiten kann.

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





## TF-IDF Modellierung:##

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

tfidf_score_per_word = TfidfTransformer().fit(BagOfWords_messages) #Anwendung des Modells auf einzelne Werte --> tfidf Score pro Unique Wort

#Plausi-Check
tfidf4=tfidf_score_per_word.transform(BagOfWords_test_4) #Anwendung des Modells auf SMS Message Nr4. als Plauscheck
word_ranking_test=(tfidf_score_per_word.idf_[BagOfWords_transformer.vocabulary_['university']])

#
tfidf_score_per_message = tfidf_score_per_word.transform(BagOfWords_messages) # Anwendung des Modells auf einzelne Message --> tfidf Score für jedes Wort für jede Message


## Modell trainieren
#Mit den Vektoren, die unsere Nachrichtne repräsentieren, kann der spam/ham Klassifizierer trainiert werden.
# Wir können tatsächlich fast jede Art an Klassifizierungs-Algorithmus verwenden. Aus verschiedenen Gründen ist der Naive Bayes Klassifzierer eine gute Wahl.
#siehe weiterführenden Link: http://www.inf.ed.ac.uk/teaching/courses/inf2b/learnnotes/inf2b-learn-note07-2up.pdf
# toller Link für verschiedene Algorithmen-Modelle: https://dbs.cs.uni-duesseldorf.de/lehre/bmarbeit/barbeiten/ba_bekcic.pdf

from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(tfidf_score_per_message, messages['label'])

#erste Prüfung
spam_detect_test = spam_detect_model.predict(tfidf4)[0] #Es wird das detect_model auf die 3 Nachricht angewendet - Output ist ham
spam_detect_test_compare=messages.label[3] # --> das Modell gibt die korrekte Klassifizierung wider.

## Daten in train & test Daten splitten
from sklearn.model_selection import train_test_split
#Pseudo_code: train_test_split= X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(messages['message'],messages['label'],test_size=0.2, random_state=101)

## Erstellung einer Daten Pipline - Speicherung von Transformationen für zukünftige Anwendungen.
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings werden in token umgewandelt und als integer count darzustellen
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])

pipeline.fit(X_train,y_train) #Modell trainieren

predictions = pipeline.predict(X_test) #Berechnung der Vorhersage
print(classification_report(predictions,y_test))#Vergleich von der Vorhersage mit den Label Daten






##Classification Report##

#    precision recall f1 - score support
#ham   1.00     0.96     0.98     1026
#spam  0.66     1.00     0.79       89

# Precision: Wie viel Prozent der Vorhersagen waren korrekt? Es gibt die Genauigkeit positiver Vorhersagen aus.
# Berechnung ham: TP / (TP + FP) (True Positive= richtig klassifizierte Message als ham; False Positive= Message als Ham, obwohl sie ein Spam ist)
# Berechnung spam: TP / (TP + FP) (True Positive= richtig klassifizierte Message als Spam; False Positive= Message als Spam, obwohl sie ein Ham ist)


# Recall: Wie viel Prozent der korrekten Vorhersgen als korrekt identifiziert worden sind.
# Berechnung ham TP/(TP+FN) (True Positive= richtig klassifizierte Message als ham, False Negative: Message als Spam klassifziert, obwohl die Message ein Ham ist.
# Berechnung spam TP/(TP+FN) (True Positive= richtig klassifizierte Message als spam, False Negative: Message als ham klassifziert, obwohl die Message ein spam ist.

# F1-Score: Wie viel Prozent der positiven Vorhersagen waren korrekt?
# Der F1-Wert ist ein gewichteter aus Recall & Precision. Der beste Wert ist 1,0 und der schlechteste beträgt 0,0.
# Im Allgemeinen sind F 1  -Werte niedriger als Genauigkeitsmaße, da sie die Precision und den Recall in ihre Berechnung einbetten.
# Berechnung f1-Score: F1 Score = 2*(Recall * Precision) / (Recall + Precision)