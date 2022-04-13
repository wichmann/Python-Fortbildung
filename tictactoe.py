
"""
Tic-Tac-Toe mit grafischer Benutzeroberfläche.

Bibliotheken:
 * pip install pyqt5

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

        # Buttons hinzufügen
        self.buttons = []
        for i in range(9):
            new_button = QtWidgets.QPushButton('')
            new_button.row = i // 3
            new_button.column = i % 3
            new_button.setMinimumSize(200, 200)
            new_button.setStyleSheet("QPushButton{font-size: 36pt;}")
            new_button.clicked.connect(self.handle_button_click)
            self.buttons.append(new_button)

        #self.button_upper_left = QtWidgets.QPushButton('')
        #self.button_upper_left.setMinimumSize(200, 200)
        # self.button_upper_left.clicked.connect(self.handle_button_click)

        # Layout setzen
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        for i, b in enumerate(self.buttons):
            layout.addWidget(b, b.row, b.column)

        self.contentWidget.setLayout(layout)
        self.setWindowTitle(app_name)
        self.setCentralWidget(self.contentWidget)

    def switch_player(self):
        if self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'

    def check_if_game_ended(self):
        checks = [[b.text() for b in self.buttons if b.row == 0],
                  [b.text() for b in self.buttons if b.row == 1],
                  [b.text() for b in self.buttons if b.row == 2],
                  [b.text() for b in self.buttons if b.column == 0],
                  [b.text() for b in self.buttons if b.column == 1],
                  [b.text() for b in self.buttons if b.column == 2],
                  [b.text() for b in self.buttons if b.column == b.row],
                  [b.text() for b in self.buttons if b.column == 2-b.row]]
        if not any(any(x == '' for x in c) for c in checks):
            return 'Unentschieden!'
        if any(all(x == 'x' for x in c) for c in checks):
            return 'x gewinnt!'
        if any(all(x == 'o' for x in c) for c in checks):
            return 'o gewinnt!'
        return ''

    def handle_button_click(self, button):
        """Zeigt eine Infobox"""
        button = self.sender()
        print('Button geklickt in Zeile {} und Spalte {}'.format(
            button.row+1, button.column+1))
        button.setText(self.current_player)
        self.switch_player()
        result = self.check_if_game_ended()
        if result:
            QtWidgets.QMessageBox.information(self, app_name, result, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app_name = 'Tic-Tac-Toe'
    app = QtWidgets.QApplication(sys.argv)
    main_window = TicTacToe()
    main_window.show()
    sys.exit(app.exec())
