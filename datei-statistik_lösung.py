
"""
Als Statistik soll die Anzahl aller Dateien eines bestimmten Dateityps innerhalb
eines Verzeichnisses und deren Dateigröße bestimmt werden. Dazu müssen zunächst
alle Dateien nach ihrer Dateiendung gefiltert werden. Anschließend müssen die
Dateigrößen aufaddiert werden. Als Ergebnis wird die Dateianzahl und die Gesamt-
größe ausgegeben.

Mögliche Erweiterungen:
Eine mögliche Erweiterung wäre es, mehrere Dateitypen zu filtern bzw. mehrere
Verzeichnisse zu durchsuchen. Außerdem könnte eine detailliertere Statistik aus-
gegeben werden.

Das Ergebnis soll nicht in Bytes, sondern in kB, MB, usw. ausgegeben werden.

Hilfen:
 * Handbuch zur walk()-Funktion der mitgelieferten Bibliothek "os" [1]
 * Artikel aus der c't [2]

Quellen:
[1] https://docs.python.org/3/library/os.html#os.walk
[2] https://www.heise.de/ratgeber/Mit-Python-Dateien-und-Verzeichnisse-beherrschen-4797849.html?seite=4#nav_verzeichnisb%C3%A4ume__1

"""


import os
import math
import fnmatch


directory = '/home/christian/'
filter_string = '*.png'


def output_size(size):
    # Source: https://stackoverflow.com/a/14822210
    if size == 0:
       return '0B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return '{} {}'.format(s, size_name[i])


def main():
    count_files = 0
    size_files = 0

    # Banner ausgeben
    print('Dateigrößenberechnung')

    # Rekursiv alle Dateien suchen, die dem Filter entsprechen und die Größe aufaddieren
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, filter_string):
            count_files += 1
            size_files += os.path.getsize(os.path.join(root, filename))

    print('Anzahl der Dateien: {}'.format(count_files))
    print('Größe der Dateien: {}'.format(output_size(size_files)))


if __name__ == '__main__':
    main()
