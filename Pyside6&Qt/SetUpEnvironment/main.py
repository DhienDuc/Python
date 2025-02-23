#VERSION1 : Setting everything up in the global scope
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show() 
app.exec()
"""

#VERSION2 : Setting up a separate class
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New App")
        button = QPushButton("Press me")
        self.setCentralWidget(button)

window = ButtonHolder()
window.show()
app.exec()
"""

#VERSION3 : Setting up a separate class in separate file
import sys
from PySide6.QtWidgets import QApplication
from btn_holder import ButtonHolder

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()