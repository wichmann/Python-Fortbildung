
"""
Es sollen alle Dateien und Unterverzeichnisse unter einem angegebenen Pfad als
ZIP-Datei gespeichert werden. Damit die Datei als Backup später wieder
eingespielt werden kann, soll der Dateiname der ZIP-Datei das aktuellen Datum
enthalten.

Mögliche Erweiterungen:

Hilfen:
 * Handbuch zur Funktion shutil.make_archive() [1]
 * Artikel aus der c't [2]

Quellen:
[1] https://docs.python.org/3/library/shutil.html#shutil.make_archive
[2] https://www.heise.de/ratgeber/Mit-Python-Dateien-und-Verzeichnisse-beherrschen-4797849.html

"""


import shutil
import datetime
from pathlib import Path


shutil.make_archive('', 'zip', '')
