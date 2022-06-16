
"""
Es soll ein Kurz-URL-Dienst [1] entwickelt werden. Dazu ist eine Web-App nötig,
die beim Aufruf eines HTTP-Endpunktes (z.B. /redirect/xxx) automatisch zu einer
vorher gespeicherten URL weiterleitet. Verschiedene Kürzel führen zu unter-
schiedlichen Internet-Adressen. Die Kurz-URL kann dann statt der kompletten,
langen URL weitergegeben werden.

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


import hashlib

from flask import Flask, request, url_for, redirect


# initialisiere HTTP-Server
app = Flask(__name__)


# erzeuge Vorlage für alle Seiten
html_template = """<html>
                     <head>
                        <title>{title}</title>
                     </head>
                     <style>
                       div a {{
                           background-color: #4CAF50;
                           border: 2px solid #aaaaaa;
                           color: white;
                           padding: 10px 32px;
                           text-align: center;
                           text-decoration: none;
                           display: inline-block;
                           font-size: 14px;
                       }}
                       div {{
                           background-color: #aaaaaa;
                           padding: 5px 5px;
                       }}
                     </style>
                     <body>
                       <h1>{heading}</h1>
                       {content}
                     </body>
                   </html>"""


saved_urls = {}


@app.route('/', methods=('GET', 'POST'))
def add_short_url():
    text = 'Generator für Kurz-URLs'
    if request.method == 'GET':
        content = """<form action="/" method="POST">
                        <label for="url">Original-URL</label><br>
                        <input type="url" id="url" name="url" size="100" />
                        <input type="submit" value="Absenden" />
                    </form>"""
        return html_template.format(title=text, heading=text, content=content)
    elif request.method == 'POST':
        original_url = request.form.get('url')
        short_url = hashlib.md5(original_url.encode('utf8')).hexdigest()[:10]
        saved_urls[short_url] = original_url
        print(saved_urls)
        content = 'Kurz-URL für <a href="{0}">{0}</a> lautet <a href="{1}">{1}</a>'.format(
            original_url, url_for('redirect_to_original_url', _external=True, shorturl=short_url))
        return html_template.format(title=text, heading=text, content=content)


@app.route('/redirect/<shorturl>')
def redirect_to_original_url(shorturl):
    if shorturl in saved_urls:
        return redirect(saved_urls[shorturl])
    else:
        title = 'Fehler'
        return html_template.format(title=title, heading=title, content='Kurz-URL existiert nicht!')


@app.route('/list')
def list_short_urls():
    title = 'Liste aller Kurz-URLs'
    content = '<br>'.join(['{} -> {}'.format(k, saved_urls[k])
                          for k in saved_urls.keys()])
    return html_template.format(title=title, heading=title, content=content)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
