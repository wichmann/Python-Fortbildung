
"""
Es ist ein Monitoring für einen Webserver eingerichtet werden. Dazu soll in
regelmäßigen Abständen eine HTTP-Anfrage zum Server geschickt werden.
Anschließend wird ein Zeitstempel, die Webadresse und die Latenz in einer CSV-
Datei abgespeichert.

Mögliche Erweiterungen:
Statt einer CSV-Datei können die Daten auch in einer JSON-Datei abgespeichert
werden. Zusätzlich könnte eine Warnung per Mail/Telegram/Signal/etc. an den
Administrator verschickt werden.

Hilfen:
 * Handbuch der Bibliothek requests [1]
 * Einführung in die Bibliothek requests [2]
 * Artikel zu requests aus dem Admin Magazin [3]

Bibliotheken:
 * requests - HTTP-Client-Bibliothek
    pip install requests

Quellen:
[1] https://requests.readthedocs.io/en/latest/
[2] https://realpython.com/python-requests/
[3] https://www.admin-magazin.de/Das-Heft/2014/04/Die-Python-Bibliothek-Requests-stellt-HTTP-Anfragen

"""


import time
import requests


wait_time = 10
url = 'https://bbs-os-brinkstr.de/'
date_file_name = 'http-monitoring.dat'


while True:
    # sende HTTP-Anfrage und speichere Latenz
    r = requests.get(url)
    roundtrip = r.elapsed.total_seconds()
    print('Latenz zu "{}" ist {} Sekunden.'.format(url, roundtrip))
    time.sleep(wait_time)
