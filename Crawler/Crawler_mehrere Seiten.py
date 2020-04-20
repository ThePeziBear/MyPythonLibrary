#Used Methods: class, def__init__, def(), urllib.parse (zur Anzeige von Bildern durch crawlen) html.parser, p.attrs, select_one (CSS-Selector), .text,

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin # verwenden für einen relativen Pfad. Abfrage von Bildern
urljoin('http://python.beispiel.programmierenlernen.io/index.php', '/img/1.jpg')



class CrawledArticle(): # Klasse repräsentiert einen einzelnen Artikel - wird  als title, emoji, content, image abgespeichert
    def __init__(self,title,emoji,content,image):
        self.title=title
        self.emoji=emoji
        self.content=content
        self.image=image


class ArticleFetcher(): # Extraktion der Artikel - die Website wird runtergeladen, Website wird geparsed und Atikel werden zurückgegeben
    def fetch(self):
        url='http://python.beispiel.programmierenlernen.io/index.php'
        r = requests.get('http://python.beispiel.programmierenlernen.io/index.php') #Hole die Website
        time.sleep(1)
        print(url)
        doc = BeautifulSoup(r.text, 'html.parser')  # Einlesen des HTML-Codes mittels parser

        articles =[] # Hole mir mit der For Schleife alle Artikel die ich benötige
        for card in doc.select('.card'): # Elemente einzeln betrachten
            emoji = card.select_one('.emoji') # Ausgabe der Emojis aller Artikel
            content = card.select_one('.card-text').text # Ausgabe des Textes
            title = card.select('.card-title span')[1].text # Ausgabe der Title
            image = urljoin(url, card.select_one('img').attrs['src']) # Ausgabe der Bilder mittels relativen link

            crawled = CrawledArticle(title, emoji, content, image)
            articles.append(crawled)

        return articles # Rückgabe der Artikel


    def nextpage(self):
        r = requests.get('http://python.beispiel.programmierenlernen.io/index.php')  # Hole die Website
        doc = BeautifulSoup(r.text, 'html.parser')  # Einlesen des HTML-Codes mittels parser
        for navigation in doc.findAll('a'):
            navigation.get('href')
        return navigation




fetcher = ArticleFetcher()
articles = fetcher.fetch() #Ausgabe der der CrawledArticles

for article in articles: # Ausgabe aller titel der Artikel
     print(article.title)

nextsite = fetcher.nextpage()
print(nextsite)

#for article in articles: # Ausgabe aller titel der Artikel
#      print(article.title)

