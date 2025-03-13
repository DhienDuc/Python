#Import
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QTableWidget, QTableWidgetItem, QComboBox, QMessageBox
from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QHeaderView
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import sys

#Design
class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()
        #Design
        self.setWindowTitle("Expense Tracker")
        self.resize(550,500)

        #Create all widget
        self.date = QDateEdit()
        self.date.setDate(QDate.currentDate())
        
        self.category = QComboBox()
        self.category.addItems(["Food", "Transport", "Entertainment", "Bills", "Others"])
        self.amount = QLineEdit()
        self.description = QLineEdit()
        self.add = QPushButton("Add Expence")
        self.add.clicked.connect(self.add_expense)
        self.delete = QPushButton("Delete Expence")
        self.delete.clicked.connect(self.delete_expense)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","Date","Category", "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #CSS styling
        self.setStyleSheet(
            """
            QWidget {
                background-color: #b8c9e1;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QLineEdit, QComboBox, QDateEdit {
                background-color: #b8c9e1;
                color: #333;
                border: 1px solid #444;
                padding: 5px;
            }
            QTableWidget {
                background-color: #b8c9e1;
                color: #333;
                border: 1px solid #444;
                selection-background-color: #ddd;
            }
            QPushButton {
                background-color: #4caf50;
                color: #fff;
                border: none;
                padding: 5px 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )

        #Layout
        master_layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        row1.addWidget(QLabel("Date"))
        row1.addWidget(self.date)
        row1.addWidget(QLabel("Category"))
        row1.addWidget(self.category)
        
        row2.addWidget(QLabel("Amount"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description"))
        row2.addWidget(self.description)

        row3.addWidget(self.add)
        row3.addWidget(self.delete)

        master_layout.addLayout(row1)
        master_layout.addLayout(row2)
        master_layout.addLayout(row3)
        master_layout.addWidget(self.table)
        self.setLayout(master_layout)

        self.load_table()

    def load_table(self):
        query = QSqlQuery()
        query.exec("SELECT * FROM expenses")
        self.table.setRowCount(0)
        while query.next():
            row = self.table.rowCount()
            self.table.insertRow(row)
            for i in range(5):
                self.table.setItem(row, i, QTableWidgetItem(str(query.value(i))))

        self.table.sortByColumn(1, Qt.DescendingOrder)

    def add_expense(self):
        #Get data
        date = self.date.date().toString("yyyy-MM-dd")
        category = self.category.currentText()
        amount = self.amount.text()
        description = self.description.text()

        if not amount or not description:
            QMessageBox.critical(None, "Error", "Please enter all fields")
            return

        #Insert data
        query = QSqlQuery()
        query.prepare("INSERT INTO expenses (date, category, amount, description) VALUES (:date, :category, :amount, :description)")
        query.bindValue(":date", date)
        query.bindValue(":category", category)
        query.bindValue(":amount", amount)
        query.bindValue(":description", description)
        if not query.exec():
            QMessageBox.critical(None, "Error", f"Database Error: {query.lastError().text()}")

        #Reset data
        self.date.setDate(QDate.currentDate())
        self.category.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

        #Load data
        self.load_table()

    def delete_expense(self):
        #Get data
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.critical(None, "Error", "Please select a row")
            return

        id = self.table.item(row, 0).text()

        result = QMessageBox.question(None, "Delete", "Are you sure you want to delete this expense?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.No:
            return

        #Delete data
        query = QSqlQuery()
        query.prepare("DELETE FROM expenses WHERE id = :id")
        query.bindValue(":id", id)
        if not query.exec():
            QMessageBox.critical(None, "Error", f"Database Error: {query.lastError().text()}")

        #Load data
        self.load_table()

#Run
app = QApplication([])

#Create Database
database  = QSqlDatabase.addDatabase("QSQLITE")
database.setDatabaseName("expense.db")
if not database.open():
    QMessageBox.critical(None, "Error", f"Database Error: {database.lastError().text()}")
    sys.exit(1)

query = QSqlQuery()
query.exec(
    """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        category TEXT,
        amount REAL,
        description TEXT
    )
    """
)

#Run
main = ExpenseTracker()
main.show()
app.exec()
