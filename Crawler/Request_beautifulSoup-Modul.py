#Used Methods: r.__dict__, r.status_code, r.text, html.parser, p.attrs, p.text, select_one (CSS-Selector), .text

# Requests Modul ermöglicht das runterladen von HTML-Code

import requests
r = requests.get('http://python.beispiel.programmierenlernen.io/index.php')
print(r.__dict__) # Eigenschaften eines Pythonobjekts auslesen
print(r.status_code) # Abfrage über den Status des Codes --> 200 bedeutet alles gut, 404 Site not found
print(r.headers) # Ausgabe von Eigenschaften der Website
print(r.text) # Ausgabe des ganzen HTML Codes


#BeautifulSoup funktionsweise
from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <p class="something">Ich bin ein Absatz!</p>
            <p>Ich bin noch ein Absatz</p>
        </body>
    </html>'
"""
doc = BeautifulSoup(html, "html.parser") # Einlesen mit Parser
for p in doc.find_all("p"):
    print(p.attrs) # Ausgabe der Attribute
    print(p.text) # Ausgabe des Textes

#Elemente im HTML finden
doc = BeautifulSoup(r.text, 'html.parser') # Einlesen des HTML-Codes
print(doc.select('.card')) # css Selektor - hole mir alle Elemente die die Klasse .card haben

for card in doc.select('.card'): # Elemente einzeln betrachten
    emoji = card.select_one('.emoji') # Ausgabe der Emojis aller Artikel
    emoji_text = card.select_one('.emoji').text  # Ausgabe des Textes -- in diesem Emoji-Symol
    content = card.select_one('.card-text').text # Ausgabe des Textes
    title_spans = card.select('.card-title span') # Ausgabe des Textes der Klasse Span
    title = title_spans[1].text # Zugriff auf den gewünschten 2 Text
    image = card.select_one('img')

    print(image.attrs['src'])
    print(emoji)
    print(content)
    print(title)

    print(card)
    break



