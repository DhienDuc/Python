#Import
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout

#Styling
from PySide6.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()

        #Design
        self.setWindowTitle("Calculator App")
        self.resize(250,350)

        #Create all widget
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))#Styling

        self.grid = QGridLayout()
        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            if text == "/" or text == "*":
                button.setStyleSheet("QPushButton {font: 25pt Comic San MS; padding: 10px; background-color : rgb(179, 64, 11); }")#Styling
            else:
                button.setStyleSheet("QPushButton {font: 25pt Comic San MS; padding: 10px; }")#Styling
            self.grid.addWidget(button, row, col)
            col += 1
            if (col > 3):
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.clear.clicked.connect(self.button_click)
        self.clear.setStyleSheet("QPushButton {font: 25pt Comic San MS; padding: 10px; }")#Styling
        self.delete = QPushButton("Del")
        self.delete.clicked.connect(self.button_click)
        self.delete.setStyleSheet("QPushButton {font: 25pt Comic San MS; padding: 10px; }")#Styling

        #Layout
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)
        master_layout.setContentsMargins(25,25,25,25)#Styling

        btn_row = QHBoxLayout()
        btn_row.addWidget(self.clear)
        btn_row.addWidget(self.delete)

        master_layout.addLayout(btn_row)
        self.setLayout(master_layout)
    
    #Function
    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                self.text_box.setText("Error!")
        elif text == "Clear":
            self.text_box.clear()
        elif text == "Del":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])
        else:
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text)

#Show/Run
if __name__ in "__main__":
    app = QApplication([])
    window = CalcApp()
    window.setStyleSheet("QWidget { background-color:rgb(31, 14, 22) }")#styling
    window.show()
    app.exec()

