
"""
Es soll ein Tic-Tac-Toe-Spiel mit grafischer Benutzeroberfläche programmiert
werden. Das Hauptfenster besteht aus neun Buttons, über die zwei Spieler
nacheinander X und O setzen können. Wenn drei gleiche Zeichen senkrecht, 
waagerecht oder diagonal nebeneinander stehen, ist das Spiel beendet.

Mögliche Erweiterungen:
Neben dem Spielfeld könnte der Spieler des aktuellen Zuges angezeigt werden.
Zusätzlich könnten mehrere Spiele nacheinander gespielt werden und der Punkte-
stand angezeigt werden.

Hilfen:
 * Referenzhandbuch für PyQt5 [1]
 * Beispielprogramm "Währungsrechner" [2]
 * Artikel aus der c't [3], [4], [5]

Bibliotheken:
 * pyQt5 - Bibliothek für grafische Benutzeroberflächen
    pip install pyqt5

Quellen:
[1] https://www.riverbankcomputing.com/static/Docs/PyQt5/
[2] https://github.com/wichmann/CurrencyCalculator/blob/master/currencyCalculator.py
[3] https://www.heise.de/ratgeber/Programmieren-mit-Python-Bedienoberflaeche-via-PyQt-erstellen-4949489.html
[4] https://www.heise.de/ratgeber/Qt-Designer-Bedienoberflaechen-fuer-Python-per-Drag-and-Drop-erstellen-6264854.html
[5] https://www.heise.de/ratgeber/Security-Simplen-Passwortgenerator-mit-Python-programmieren-6296784.html

"""


import sys

from PyQt5 import QtWidgets


class TicTacToe(QtWidgets.QMainWindow):
    """Hauptfenster für Währungsrechner"""

    current_player = 'x'

    def __init__(self):
        """Initialisierung von Hauptfenster"""
        QtWidgets.QMainWindow.__init__(self)
        self.contentWidget = QtWidgets.QWidget()
        self.titleLabel = QtWidgets.QLabel(app_name)
        self.setMinimumSize(640, 640)

        # Layout setzen
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Button hinzufügen
        new_button = QtWidgets.QPushButton('')
        new_button.setMinimumSize(200, 200)
        new_button.setMaximumSize(200, 200)
        new_button.setStyleSheet("QPushButton{font-size: 36pt;}")
        new_button.clicked.connect(self.handle_button_click)
        layout.addWidget(new_button, 0, 0)

        self.contentWidget.setLayout(layout)
        self.setWindowTitle(app_name)
        self.setCentralWidget(self.contentWidget)


    def handle_button_click(self, button):
        """Zeigt eine Infobox"""
        print('Button geklickt!')
        QtWidgets.QMessageBox.information(self, app_name, 'Button geklickt!', QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app_name = 'Tic-Tac-Toe'
    app = QtWidgets.QApplication(sys.argv)
    main_window = TicTacToe()
    main_window.show()
    sys.exit(app.exec())
