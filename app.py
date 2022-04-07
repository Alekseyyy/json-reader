
# Simple JSON Reading App
# Written by A. S. "Aleksey" Ahmann <hackermaneia@riseup.com>
# - GitHub: https://github.com/Alekseyyy

import sys
import json

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, 
    QMessageBox, QFileDialog
)

from PyQt5.uic import loadUi
from dialogs.main import Ui_MainWindow

class JSONReader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionExit.triggered.connect(self.close)
        self.actionAbout_2.triggered.connect(self.about)
        self.actionOpen_2.triggered.connect(self.openJSON)
        
    # functions that I have defined
    
    def exit(self):
        sys.exit(0)
        
    def about(self):
        QMessageBox.about(self, "Simple JSON Reader",
        """
        <p>The simple JSON reader was created by Aleksey (github/@Alekseyyy)</p>
        <p>Check out the project repo for some help on using it:</p>
        <p>&bull; <a href="https://github.com/Alekseyyy/json-reader">https://github.com/Alekseyyy/json-reader</a></p>
        """)
        
    def openJSON(self):
        fod = QFileDialog().getOpenFileName(
            self, "Open JSON File", ".", "JSON Files (*.json)")
        # print (fod[0])
        pass

def main():
    app = QApplication(sys.argv)
    jr = JSONReader()
    jr.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
