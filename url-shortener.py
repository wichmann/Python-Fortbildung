
"""
Eine Webserver, der Kurz-URLs erstellt und beim Aufruf zur Original-Seite weiterleitet.

Bibliotheken:
 * pip install flask

Quellen:
 * https://flask.palletsprojects.com/en/2.0.x/

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
        content = 'Kurz-URL für <a href="{0}">{0}</a> lautet <a href="{1}">{1}</a>'.format(original_url, url_for('redirect_to_original_url', _external=True, shorturl=short_url))
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
    content = '<br>'.join(['{} -> {}'.format(k, saved_urls[k]) for k in saved_urls.keys()])
    return html_template.format(title=title, heading=title, content=content)


if __name__ == '__main__':
    #app.debug = True
    app.run(host= '0.0.0.0', port=5000)
