
"""
Die beiliegende CSV-Datei enthält einen Auszug aus der Hardwareliste des
Schulserver. In der Liste sind alle Rechner inventarisiert und mit Angaben zu
Board, CPU, Hauptspeicher, Festplatte, Netzwerk versehen.

Lesen Sie die Datei mit der mitgelieferten Bibliothek "csv" ein und finden Sie
alle Rechner in Haus C, deren Festplatte für das aktuelle Betriebssystemimage
zu klein ist (<512GB).

Mögliche Erweiterungen:
Es wäre auch möglich, nach dem Alter (über die CPU-Generation), der
Geschwindigkeit der Netzwerkkarte oder dem Hauptspeicher zu filtern. Die Ausgabe
des Programms könnte mit der Bibliothek "tabulate" schöner gestaltet werden.

Hilfen:
 * Handbuch zur mitgelieferten Bibliothek "csv" [1]

Quellen:
[1] https://docs.python.org/3/library/csv.html

"""


import csv

from tabulate import tabulate


dateiname = 'hardwareliste_daten.csv'


data = []

with open(dateiname, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=';')
    for zeile in csv_reader:
        # Hersteller: zeile['System Hersteller']
        # Gerätename: zeile['Gerät']
        # Standort: zeile['Standort']
        # Festplatte: zeile['Disk 0 Größe']
        # Hauptspeicher: zeile['Memory 0 Größe'], zeile['Memory 1 Größe'], zeile['Memory 2 Größe']

        # Filtere Haus C aus
        if not zeile['Standort'].startswith('r2'):
            continue

        # Berechne gesamten Hauptspeicher
        hauptspeicher = []
        speicher0 = zeile['Memory 0 Größe']
        speicher1 = zeile['Memory 1 Größe']
        speicher2 = zeile['Memory 2 Größe']
        try:
            hauptspeicher.append(int(speicher0.split()[0]))
            hauptspeicher.append(int(speicher1.split()[0]))
            hauptspeicher.append(int(speicher2.split()[0]))
        except:
            pass

        # Prüfe Größe der Platte
        festplatte = int(zeile['Disk 0 Größe'].split()[0])
        if festplatte < 512:
            data.append((zeile['Gerät'], zeile['System Hersteller'], festplatte, hauptspeicher))

print(tabulate(data, ['Gerät', 'System Hersteller', 'Festplatte (GB)', 'Hauptspeicher (GB)'], tablefmt="grid"))
