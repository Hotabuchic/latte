# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 532)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(60, 20, 401, 31))
        self.id.setReadOnly(False)
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(100, 70, 361, 31))
        self.name.setReadOnly(False)
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 121, 21))
        self.label_3.setObjectName("label_3")
        self.roasting = QtWidgets.QLineEdit(Dialog)
        self.roasting.setGeometry(QtCore.QRect(140, 130, 321, 31))
        self.roasting.setReadOnly(False)
        self.roasting.setObjectName("roasting")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 61, 21))
        self.label_4.setObjectName("label_4")
        self.yes = QtWidgets.QRadioButton(Dialog)
        self.yes.setGeometry(QtCore.QRect(120, 180, 51, 18))
        self.yes.setCheckable(True)
        self.yes.setChecked(False)
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QRadioButton(Dialog)
        self.no.setGeometry(QtCore.QRect(190, 180, 61, 18))
        self.no.setObjectName("no")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 71, 16))
        self.label_5.setObjectName("label_5")
        self.description = QtWidgets.QTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(100, 230, 371, 131))
        self.description.setObjectName("description")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 380, 47, 21))
        self.label_6.setObjectName("label_6")
        self.price = QtWidgets.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(90, 380, 381, 31))
        self.price.setObjectName("price")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 440, 111, 21))
        self.label_7.setObjectName("label_7")
        self.amount = QtWidgets.QLineEdit(Dialog)
        self.amount.setGeometry(QtCore.QRect(130, 440, 331, 31))
        self.amount.setObjectName("amount")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(230, 490, 81, 31))
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(350, 490, 75, 31))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Изменение/Добавление"))
        self.label.setText(_translate("Dialog", "id:"))
        self.label_2.setText(_translate("Dialog", "Название:"))
        self.label_3.setText(_translate("Dialog", "Cтепень обжарки"))
        self.label_4.setText(_translate("Dialog", "Молотый:"))
        self.yes.setText(_translate("Dialog", "Да"))
        self.no.setText(_translate("Dialog", "Нет"))
        self.label_5.setText(_translate("Dialog", "Описание:"))
        self.label_6.setText(_translate("Dialog", "Цена:"))
        self.label_7.setText(_translate("Dialog", "Объем упаковки:"))
        self.ok.setText(_translate("Dialog", "ОК"))
        self.cancel.setText(_translate("Dialog", "ОТМЕНА"))
