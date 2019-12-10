import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from main_window import Ui_MainWindow
import requests
import json

"""
The ip of the rest server (must contain http / https)
"""
ip = "http://localhost:8080"

"""
This methode translates the given text and returns:
- an error message, formatted as html
- the language, probability and reliability formatted as html
"""
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
    except:
        return "Wrong response from server - is your input correct?"


"""
The controller, which starts the GUI and defines what happens when the "check" button is pressed
"""
class Controller(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage("Waiting for input...")
        self.ui.checkButton.pressed.connect(lambda: self.get_lang())

    def get_lang(self):
        """
           sets the result field to the output of text and displays a status message in the statusbar
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


"""
Start the Controller and wait for it to exit
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
