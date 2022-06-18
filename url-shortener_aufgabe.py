
"""
Es soll ein Kurz-URL-Dienst [1] entwickelt werden. Dazu ist eine Web-App nötig,
die beim Aufruf eines HTTP-Endpunktes (z.B. /redirect/xxx) automatisch zu einer
vorher gespeicherten URL weiterleitet. Verschiedene Kürzel führen zu unter-
schiedlichen Internet-Adressen. Die Kurz-URL kann dann statt der kompletten,
langen URL weitergegeben werden.

Für die Speicherung der Zuordnung zwischen Kurz-URL und Lang-URL kann ein
Dictionary genutzt werden. Alternativ wäre die Speicherung in einer SQLite-
Datenbank möglich.

Mögliche Erweiterungen:
Neben dem Endpunkt zur Weiterleitung gibt es einen Server-Pfad, über den neue
Weiterleitungen eingerichtet werden können. Zur Verwaltung des Servers wäre
eine Übersichtsseite sinnvoll, auf der alle Kurz-URLs aufgelistet werden.

Hilfen:
 * Handbuch des Pakets Flask [2]
 * Einführender Artikel zu Flask [3]

Bibliotheken:
 * Flask - Leichtgewichtiges Web Application Framework
    pip install flask

Quellen:
[1] https://de.wikipedia.org/wiki/Kurz-URL-Dienst
[2] https://flask.palletsprojects.com/en/2.1.x/
[3] https://www.heise.de/ratgeber/Python-Framework-fuer-Webentwicklung-Einfacher-Einstieg-mit-Flask-6340642.html

"""


from flask import Flask


# initialisiere HTTP-Server
app = Flask(__name__)


# erzeuge Vorlage für alle Seiten
html_template = """<html>
                     <head>
                        <title>{title}</title>
                     </head>
                     <body>
                       <h1>{heading}</h1>
                       {content}
                     </body>
                   </html>"""


@app.route('/', methods=['GET'])
def index():
    text = 'Generator für Kurz-URLs'
    content = 'Herzlich Willkommen...'
    return html_template.format(title=text, heading=text, content=content)


@app.route('/redirect/<shorturl>')
def redirect_to_original_url(shorturl):
    pass


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
