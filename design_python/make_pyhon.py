# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/make_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Make_an_order(object):
    def setupUi(self, Make_an_order):
        Make_an_order.setObjectName("Make_an_order")
        Make_an_order.resize(800, 727)
        self.centralwidget = QtWidgets.QWidget(Make_an_order)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 611, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.make_button = QtWidgets.QPushButton(self.centralwidget)
        self.make_button.setGeometry(QtCore.QRect(30, 320, 611, 26))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(18)
        self.make_button.setFont(font)
        self.make_button.setObjectName("make_button")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 410, 351, 271))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 370, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Make_an_order.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Make_an_order)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Make_an_order.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Make_an_order)
        self.statusbar.setObjectName("statusbar")
        Make_an_order.setStatusBar(self.statusbar)

        self.retranslateUi(Make_an_order)
        QtCore.QMetaObject.connectSlotsByName(Make_an_order)

    def retranslateUi(self, Make_an_order):
        _translate = QtCore.QCoreApplication.translate
        Make_an_order.setWindowTitle(_translate("Make_an_order", "Сделать заказ"))
        self.make_button.setText(_translate("Make_an_order", "Заказать"))
        self.label.setText(_translate("Make_an_order", "Итог:"))