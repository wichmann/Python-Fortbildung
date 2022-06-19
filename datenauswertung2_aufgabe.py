
"""
Die Datei datenauswertung2_daten.csv enthält die einen Zeitstempel und die
Latenz für den Aufruf des Moodles der BBS Brinkstraße seit April 2018.

Es soll für einen vorgegebenen Zeitraum eine Heatmap erstellt werden, die die
Latenz visualisiert. Damit lassen sich Ausfallzeiten schnell finden und Belas-
tungssituationen des Servers leicht ausfindig machen. Für die Visualisierung
bietet sich die Bibliothek "seaborn" [1] an.

Mögliche Erweiterungen:
Statt "seaborn" könnte die Bibliothek "Bokeh" [6] genutzt werden, die Visuali-
sierungen mit HTML und Javascript ermöglicht, die direkt im Browser angesehen
werden können. Diese Bibliothek liefert zum Testen viele Beispieldaten mit.

Hilfen:
 * Webseite der Bibliothek "seaborn" [1]
 * Einführung in die Bibliothek "pandas" [2]
 * Artikel von heise zu "Analyse von Open Data mit Pandas" [3]
 * Artikel aus der c't "Mit Python und Pandas die eigenen Einkaufsdaten analysieren" [4]
 * Beispieldaten von den Machern der Bibliothek "pandas" [5]

Bibliotheken:
 * pandas - Datenanalyse und -manipulation
    pip install pandas
 * matplotlib - Erstellung von Diagrammen
    pip install matplotlib
 * seaborn - Statistische Visualisierungen
    pip install seaborn
 * numpy - Numerische Mathematik
    pip install matplotlib

Quellen:
[1] https://seaborn.pydata.org/
[2] https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
[3] https://www.heise.de/hintergrund/Analyse-von-Open-Data-mit-Pandas-5049049.html
[4] https://www.heise.de/ratgeber/Mit-Python-und-Pandas-die-eigenen-Einkaufsdaten-analysieren-6668748.html
[5] https://github.com/pandas-dev/pandas/tree/main/doc/data
[6] https://pypi.org/project/bokeh/

"""


import numpy as np
import pandas as pd
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import seaborn as sns


datendatei = 'datenauswertung2_daten.csv.gz'


def lade_daten(start_datum='', end_datum=''):
    latenz_daten = pd.read_csv(datendatei, parse_dates=[0], names=['timestamp', 'latency'], index_col='timestamp')
    latenz_daten = latenz_daten.resample('10Min').apply(np.median)
    latenz_daten = latenz_daten.fillna(value=5)
    if start_datum and end_datum:
        latenz_daten = latenz_daten[start_datum:end_datum]
    return latenz_daten


def erstelle_heatmap(latenz_daten):
    pass


if __name__ == '__main__':
    latenz_daten = lade_daten(start_datum='2021-04-01', end_datum='2021-06-30')
    erstelle_heatmap(latenz_daten)
