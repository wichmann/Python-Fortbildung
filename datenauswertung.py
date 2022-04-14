
"""
Einfache Datenauswertung und Ausgabe von Daten. Schreiben der Daten in Excel-Datei???

Bibliotheken:
 * pip install pandas
 * pip install matplotlib

Quellen:
 * Tutorial: https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
 * Beispieldaten: https://github.com/pandas-dev/pandas/tree/main/doc/data
 * Datenquelle der CSV-Datei: https://databank.worldbank.org/data/reports.aspx?dsid=2&series=IT.NET.USER.ZS

"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


daten = pd.read_csv('datenauswertung.csv', index_col='Country Code')
gesuchte_laender = ['Germany', 'United States', 'France', 'Poland', 'United Kingdom', 'Sweden', 'Switzerland']
zeitreihe_deutschland = daten[daten['Country Name'].isin(gesuchte_laender)]
zeitreihe_deutschland.drop(['Series Name', 'Series Code', 'Country Name'], axis=1, inplace=True)
kurve = zeitreihe_deutschland.transpose().plot()
plt.xlabel('Jahre')
plt.title('Anteil der Internetnutzer in verschiedenen Ländern')
plt.ylabel('Anteil Internetnutzer in Prozent')
plt.grid()
plt.show() 
