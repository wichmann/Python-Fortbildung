
"""
Die Datei datenauswertung.csv enthält den Anteil der Internetnutzer in ver-
schiedenen Ländern an der Gesamtbevölkerung über die Jahre von 2002 bis 2021
(Datenquelle: Statistikdatenbank der Weltbank [1]). Es soll für eine ausge-
wählte Anzahl von Ländern ein Liniendiagramm erstellt werden, das den Verlauf
des Anteils über die gegebenen Jahre darstellt.

Mögliche Erweiterungen:

Hilfen:
 * Einführung in die Bibliothek "pandas" [2]
 * Artikel von heise zu "Analyse von Open Data mit Pandas" [3]
 * Artikel aus der c't "Mit Python und Pandas die eigenen Einkaufsdaten analysieren" [4]
 * Beispieldaten von den Machern der Bibliothek "pandas" [5]

Bibliotheken:
 * pandas - 
    pip install pandas
 * matplotlib - Erstellung von Diagrammen
    pip install matplotlib

Quellen:
[1] https://databank.worldbank.org/data/reports.aspx?dsid=2&series=IT.NET.USER.ZS
[2] https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
[3] https://www.heise.de/hintergrund/Analyse-von-Open-Data-mit-Pandas-5049049.html
[4] https://www.heise.de/ratgeber/Mit-Python-und-Pandas-die-eigenen-Einkaufsdaten-analysieren-6668748.html
[5] https://github.com/pandas-dev/pandas/tree/main/doc/data

"""


import pandas as pd
import matplotlib.pyplot as plt


daten = pd.read_csv('datenauswertung_daten.csv', index_col='Country Code')
gesuchte_laender = ['Germany', 'United States', 'France', 'Poland', 'United Kingdom', 'Sweden', 'Switzerland']
