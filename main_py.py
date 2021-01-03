import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from addEditCoffeeForm_py import AddEditCoffeeForm


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.refresh()
        self.initUI()

    def refresh(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.data = list(self.cur.execute("SELECT * FROM coffee").fetchall())
        self.table.setRowCount(len(self.data))
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.table.setItem(i, j, QTableWidgetItem(str(self.data[i][j])))
        self.con.close()

    def initUI(self):
        self.add.clicked.connect(self.do)
        self.change.clicked.connect(self.do)

    def do(self):
        button = self.sender().text()
        data = None
        if button == "Изменить":
            data = self.data[self.table.currentRow()]
        edit = AddEditCoffeeForm(data)
        edit.show()
        edit.exec()
        self.refresh()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
