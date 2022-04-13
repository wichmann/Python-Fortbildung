
"""
Auslesen der Benzinpreis-Datenbank (Markttransparenzstelle für Kraftstoffe) und
Ausgabe der aktuell günstigsten fünf Tankstellen.

Bibliotheken:
 * pip install requests
 * pip install tabulate

Quellen:
 * https://creativecommons.tankerkoenig.de/?page=info

"""


import requests
from tabulate import tabulate


def main():
    parameter = {
        'lat': 52.4202, # Breitengrad
        'lng': 8.0005,  # Längengrad
        'type': 'e10',  # Art des Kraftstoffs: diesel, e5, e10, all
        'apikey': 'd30e3874-19f8-1af1-1291-ec5d7efa5297',
        'sort': 'price',
        'rad': 5      # Radius der Suche
    }
    url = 'https://creativecommons.tankerkoenig.de/json/list.php'
    r = requests.get(url, params=parameter)
    data = []
    for s in r.json()['stations']:
        data.append((s['name'], s['dist'], s['price']))
    print(tabulate(data, ['Name', 'Entfernung', 'Preis'], tablefmt="grid"))


if __name__ == '__main__':
    main()
