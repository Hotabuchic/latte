import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class AddEditCoffeeForm(QDialog):
    def __init__(self, data):
        super().__init__()
        self.data = data
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.initUI()

    def initUI(self):
        self.id.setEnabled(False)
        if self.data is not None:
            self.id.setText(str(self.data[0]))
            self.idd = self.data[0]
            self.name.setText(str(self.data[1]))
            self.roasting.setText(str(self.data[2]))
            if self.data[3] == "True":
                self.yes.setChecked(True)
            else:
                self.no.setChecked(True)
            self.description.setText(str(self.data[4]))
            self.price.setText(str(self.data[5]))
            self.amount.setText(str(self.data[6]))
        self.ok.clicked.connect(self.do)
        self.cancel.clicked.connect(self.exit)

    def do(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        ground = "True"
        if self.no.isChecked():
            ground = "False"
        if self.data is not None:
            cur.execute("UPDATE coffee SET name = ?, roasting = ?, ground = ?, taste = ?,"
                        " price = ?, amount = ? WHERE id = ?",
                        (self.name.text(), self.roasting.text(),
                         ground, self.description.toPlainText(),
                         self.price.text(), self.amount.text(), self.idd))
        else:
            cur.execute("INSERT INTO coffee(name, roasting, ground, taste, price, amount)"
                        " VALUES(?, ?, ?, ?, ?, ?)", (self.name.text(), self.roasting.text(),
                                                      ground, self.description.toPlainText(),
                                                      self.price.text(), self.amount.text()))
        con.commit()
        con.close()
        self.close()

    def exit(self):
        self.close()
