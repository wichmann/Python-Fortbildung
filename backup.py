
"""
Backup eines Verzeichnisses und Ablegen als ZIP-Datei mit dem aktuellen Datum im Namen.

Bibliotheken:
 * 

Quellen:
 * https://docs.python.org/3/library/shutil.html#shutil.make_archive

"""


import shutil
import datetime
from pathlib import Path


zu_sicherndes_verzeichnis = Path('.')
heute = datetime.datetime.now()
zip_datei = Path('..') / 'backup_{}'.format(heute.strftime('%Y-%m-%d'))
shutil.make_archive(zip_datei, 'zip', zu_sicherndes_verzeichnis)
