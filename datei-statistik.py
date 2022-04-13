
"""
Suchen aller Dateien eines bestimmten Dateityps innerhalb eines Verzeichnisses
und Ausgabe der Gesamtgröße aller gefundenen Dateien.
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
