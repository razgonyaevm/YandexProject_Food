# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/hello_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Hello_Window(object):
    def setupUi(self, Hello_Window):
        Hello_Window.setObjectName("Hello_Window")
        Hello_Window.resize(605, 464)
        Hello_Window.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(Hello_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 80, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 0, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 150, 234, 92))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.change = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.change.setObjectName("change")
        self.verticalLayout.addWidget(self.change)
        self.remove = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 270, 231, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.make_order = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.make_order.setObjectName("make_order")
        self.verticalLayout_2.addWidget(self.make_order)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_2.addWidget(self.exit_button)
        Hello_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hello_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 21))
        self.menubar.setObjectName("menubar")
        Hello_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hello_Window)
        self.statusbar.setObjectName("statusbar")
        Hello_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Hello_Window)
        QtCore.QMetaObject.connectSlotsByName(Hello_Window)

    def retranslateUi(self, Hello_Window):
        _translate = QtCore.QCoreApplication.translate
        Hello_Window.setWindowTitle(_translate("Hello_Window", "Добро пожаловать!"))
        self.label.setText(_translate("Hello_Window", "Выберите, что вы хотите сделать"))
        self.label_2.setText(_translate("Hello_Window", "Добро пожаловать!"))
        self.change.setText(_translate("Hello_Window", "Изменить элементы базы данных"))
        self.remove.setText(_translate("Hello_Window", "Удалить элементы из базы данных"))
        self.add.setText(_translate("Hello_Window", "Добавить элементы в базу данных"))
        self.make_order.setText(_translate("Hello_Window", "Сделать заказ"))
        self.exit_button.setText(_translate("Hello_Window", "Выйти"))