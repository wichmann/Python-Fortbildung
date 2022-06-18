
"""
Alle Tankstellen in Deutschland melden ihre Preise regelmäßig an eine zentrale
Benzinpreis-Datenbank (Markttransparenzstelle für Kraftstoffe). Über eine REST-
HTTP-Schnittstelle von tankerkoenig.de [1] lassen sich diese Preisinformationen
auslesen. Die Antwort des Servers enthält JSON-Daten, die sich einfach aus-
werten und weiterverarbeiten lassen.

Es sollen die Preise der Tankstellen um einen bestimmten Ort herum abgerufen
werden. Anschließend sollen die aktuell fünf günstigsten Tankstellen in über-
sichtlicher Tabellenform ausgegeben werden.

Mögliche Erweiterungen:


Hilfen:
 * Handbuch der Bibliothek requests [2]
 * Einführung in die Bibliothek requests [4]
 * Hinweise zur Nutzung der Bibliothek tabulate [3]
 * Artikel zu requests aus dem Admin Magazin [5]

Bibliotheken:
 * requests - HTTP-Client-Bibliothek
    pip install requests
 * tabulate - Ausgabe von schönen Tabellen auf der Kommandozeile
    pip install tabulate

Quellen:
[1] https://creativecommons.tankerkoenig.de/?page=info
[2] https://requests.readthedocs.io/en/latest/
[3] https://github.com/astanin/python-tabulate#library-usage
[4] https://realpython.com/python-requests/
[5] https://www.admin-magazin.de/Das-Heft/2014/04/Die-Python-Bibliothek-Requests-stellt-HTTP-Anfragen

"""


import requests
from tabulate import tabulate


parameter = {
    'lat': 52.4202, # Breitengrad
    'lng': 8.0005,  # Längengrad
    'type': 'e10',  # Art des Kraftstoffs: diesel, e5, e10, all
    'apikey': 'd30e3874-19f8-1af1-1291-ec5d7efa5297',
    'sort': 'price',
    'rad': 15      # Radius der Suche
}
url = 'https://creativecommons.tankerkoenig.de/json/list.php'
r = requests.get(url, params=parameter)
print(r.text)
