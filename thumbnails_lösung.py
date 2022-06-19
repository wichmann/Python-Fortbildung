
""" 
Es soll für alle Bild-Dateien in einem Verzeichnis ein Thumbnail erzeugt
werden. Die Vorschaubilder sollen eine Größe von maximal 128 Pixel besitzen
und im Namen das Wort "thumbnail" ergänzen. So würde aus der Bilddatei
"bild.jpeg" die Datei "bild.thumbnail.jpeg".

Für die Bildbearbeitung kann die Python-Bibliothek Python Imaging Library
(Pillow) verwendet werden. Diese bietet die Funktion thumbnail() speziell für
die Erstellung der Vorschaubildern.

Mögliche Erweiterungen:
Weitere Bildbearbeitungsschritte wären möglich, wie zum Beispiel die Umwandlung
in Graustufenbilder, Ausschnittsvergrößerungen, etc. (siehe [2]).

Hilfen:
 * Handbuch zur Biliothek "Pillow" [1]
 * Artikel von heise zur Bibliothek "Pillow für Einsteiger: So bearbeiten Sie
   Bilder mit Python" [2]

Bibliotheken:
 * Pillow - Python Imaging Library
    pip install Pillow

Quellen:
[1] https://pillow.readthedocs.io/en/latest/handbook/index.html
[2] https://www.heise.de/ratgeber/Pillow-fuer-Einsteiger-So-bearbeiten-Sie-Bilder-mit-Python-7091653.html

"""


import os
import pathlib

from PIL import Image


verzeichnis = './bilder'
size = 128, 128


for datei in pathlib.Path(verzeichnis).glob(pattern='*'):
    ausgabe_datei = os.path.splitext(datei)[0] + ".thumbnail.jpeg"
    if datei != ausgabe_datei:
        try:
            im = Image.open(datei)
            im.thumbnail(size)
            im.save(ausgabe_datei, "JPEG")
        except IOError:
            print(f'Thumbnail für Datei {datei} konnte nicht erzeugt werden!')
