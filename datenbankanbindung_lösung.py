
"""
Eine bestehende MariaDB-Datenbank soll per SQL abgefragt werden. Die Ergebnisse
sind tabellarisch auf der Konsole auszugeben.

Bevor das Python-Programm ausgeführt wird, muss zunächst MariaDB gestartet
werden. Auf den Schulrechnern kann dies über das XAMPP Control Panel geschehen.

Mögliche Erweiterungen:

Hilfen:
 * Handbuch zum MariaDB-Connector für Python [2]
 * Blog-Eintrag "How to connect Python programs to MariaDB" [3]
 * Hinweise zur Nutzung der Bibliothek tabulate [4]

Bibliotheken:
 * MariaDB - Datenbankschnittstelle zu MariaDB
    pip install mariadb
 * tabulate - Ausgabe von schönen Tabellen auf der Kommandozeile
    pip install tabulate

Quellen:
[1] https://www.github.com/mariadb-corporation/mariadb-connector-python
[2] https://mariadb-corporation.github.io/mariadb-connector-python/
[3] https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/
[4] https://github.com/astanin/python-tabulate#library-usage

"""

import sys

import mariadb
from tabulate import tabulate


try:
    # Verbindung aufbauen
    connection = mariadb.connect(
        user='root',
        password='',
        host='127.0.0.1',
        port=3306
    )
    cursor = connection.cursor()

    # Tabelle anlegen und mit Daten füllen
    cursor.execute('USE test')
    cursor.execute('CREATE TABLE IF NOT EXISTS students (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY (id) )')
    cursor.execute('INSERT INTO students VALUES (0, "Christian Wichmann")')
    connection.commit()

    # Tabelle abfragen und Ergebnisse ausgeben
    cursor.execute('SELECT * FROM students')
    ergebnisse = cursor.fetchall()
    print(tabulate(ergebnisse, ['ID', 'Name'], tablefmt="grid"))
    
    # Verbindung schließen
    cursor.close()
    connection.close()

except mariadb.Error as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)
