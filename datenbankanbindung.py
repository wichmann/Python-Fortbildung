
"""
Abfragen einer MariaDB-Datenbank.

Bibliotheken:
 * pip install mariadb
 * pip install tabulate

Vorgehen:
 * Starten Sie das XAMPP Control Panel und dort den MySQL-Server.
 * ???

Quellen:
 * https://www.github.com/mariadb-corporation/mariadb-connector-python
 * https://mariadb-corporation.github.io/mariadb-connector-python/index.html
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
