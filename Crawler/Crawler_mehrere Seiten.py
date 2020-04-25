#Used Methods: class, def__init__, def(), urllib.parse (zur Anzeige von Bildern durch crawlen) html.parser, p.attrs, select_one (CSS-Selector), .text, csv- Import

import time
from urllib.parse import urljoin  # verwenden für einen relativen Pfad. Abfrage von Bildern

import requests
from bs4 import BeautifulSoup


urljoin('http://python.beispiel.programmierenlernen.io/index.php', '/img/1.jpg')



class CrawledArticle(): # Klasse repräsentiert einen einzelnen Artikel - wird  als title, emoji, content, image abgespeichert
    def __init__(self,title,emoji,content,image):
        self.title=title
        self.emoji=emoji
        self.content=content
        self.image=image


class ArticleFetcher(): # Extraktion der Artikel - die Website wird runtergeladen, Website wird geparsed und Atikel werden zurückgegeben
    def fetch(self):
        url='http://python.beispiel.programmierenlernen.io/index.php' #Initiale Adresse für das Abrufen
        time.sleep(1)

        articles = []  # Hole mir mit der For Schleife alle Artikel die ich benötige in eine leere Liste

        while url != '': # While Schleife mit Ungleich - Rufe Solange die Website ab solange ein Button verfügbar ist.
            print(url)
            time.sleep(1)
            r = requests.get(url)  # Hole die url
            doc = BeautifulSoup(r.text, 'html.parser')  # Einlesen des HTML-Codes mittels parser

            for card in doc.select('.card'): # Auslesen der einzelnen Artikel
                emoji = card.select_one('.emoji') # Ausgabe der Emojis aller Artikel
                content = card.select_one('.card-text').text # Ausgabe des Textes
                title = card.select('.card-title span')[1].text # Ausgabe der Title
                image = urljoin(url, card.select_one('img').attrs['src']) # Ausgabe der Bilder aufgrund von urljoin wird der link absolut gesetzt

                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)

            next_button = doc.select_one('.navigation .btn')# Abrufen des relativen Links für den Button 'NÄCHSTE SEITE'
            if next_button: # If Bedingung für Schleife für "Solange ein "Button" verfügbar ist
                next_link = next_button.attrs['href'] #Abrufen des relativen Links für den Button 'NÄCHSTE SEITE'
                next_href = urljoin(url, next_link) # Abrufen des absoluten Links
                url = next_href
            else:
                url = ''


        return articles # Rückgabe der Artikel


    #def nextpage(self):
    #    r = requests.get('http://python.beispiel.programmierenlernen.io/index.php')  # Hole die Website
    #    doc = BeautifulSoup(r.text, 'html.parser')  # Einlesen des HTML-Codes mittels parser

    #    for navigation in doc.findAll('a'):
    #        navigation.get('href')
    #    return navigation




fetcher = ArticleFetcher()
articles = fetcher.fetch() #Ausgabe der der CrawledArticles

for article in articles: # Ausgabe aller titel der Artikel
     print(article.title)

fetcher = ArticleFetcher()

import csv
with open('crawler_output.csv', 'w', newline='') as csvfile: # Benennen der csvDatei
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL) # Einstellungen für die Ausgabe

    for article in fetcher.fetch(): #für jeden Artikel von meinen extrahierten Artikel
        articlewriter.writerow([article.emoji,article.title, article.image, article.content])
