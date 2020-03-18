#Used Methods: r.__dict__, r.status_code, r.text, html.parser, p.attrs, p.text

# Requests Modul ermöglicht das runterladen von HTML-Code

import requests
r = requests.get('http://python.beispiel.programmierenlernen.io/index.php')
print(r.__dict__) # Eigenschaften eines Pythonobjekts auslesen
print(r.status_code) # Abfrage über den Status des Codes --> 200 bedeutet alles gut, 404 Site not found
print(r.headers) # Ausgabe von Eigenschaften der Website
print(r.text) # Ausgabe des ganzen HTML Codes

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

doc = BeautifulSoup(r.text, 'html.parser') # Einlesen des HTML-Codes
print(doc.select('.card'))



