import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from main_window import Ui_MainWindow
import requests
import json

ip = "http://localhost:8080"


def translate(text):
    try:
        resp = requests.get(ip + "/?text=" + text)
    except:
        return "<b>Cannot establish connection to server</b>"
    try:
        r = resp.json()
        lang = str(r["language"])
        reliable = r["reliable"]
        probability = str(r["prob"])
        string = ""
        if reliable==True:
            string += "reliable: <b>yes</b><br>"
        else:
            string += "reliable: <b>no</b><br>"
        string += "language: <b>" + lang + "</b><br>"
        string += "probability: <b>" + probability + "%</b>"
        return string
    except Exception as e:
        return "Wrong response from server - is your input correct?" + e


class Controller(QMainWindow):
    """
    Ein controller welcher output.py und die Konvertierer implementiert
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("Waiting for input...")
        self.ui.checkButton.pressed.connect(lambda: self.get_lang())

    def get_lang(self):
        """
           wird ausgeführt sobald der Button 'check' gedrückt wird
       """
        self.ui.statusbar.showMessage("Guessing Lang...")
        message = "Languege guessed"
        try:
            text = self.ui.textInput.toPlainText()
            print(text)
            response = translate(text)
            self.ui.textBrowser.setText(response)
        except Exception as e:
            print(e)
            message = str(e)
        self.ui.statusbar.showMessage(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
