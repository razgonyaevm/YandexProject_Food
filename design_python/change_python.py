# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/change_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_database(object):
    def setupUi(self, Change_database):
        Change_database.setObjectName("Change_database")
        Change_database.resize(641, 620)
        self.centralwidget = QtWidgets.QWidget(Change_database)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 591, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(42)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(37, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(38, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(39, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(40, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(41, item)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(130, 430, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Times")
        self.save_button.setFont(font)
        self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_button.setStyleSheet("border-radius: 50px;")
        self.save_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon)
        self.save_button.setIconSize(QtCore.QSize(70, 70))
        self.save_button.setFlat(True)
        self.save_button.setObjectName("save_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(400, 430, 71, 71))
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setStyleSheet("border-radius: 50px;")
        self.exit_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QtCore.QSize(70, 70))
        self.exit_button.setFlat(True)
        self.exit_button.setObjectName("exit_button")
        Change_database.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Change_database)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 21))
        self.menubar.setObjectName("menubar")
        Change_database.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Change_database)
        self.statusbar.setObjectName("statusbar")
        Change_database.setStatusBar(self.statusbar)

        self.retranslateUi(Change_database)
        QtCore.QMetaObject.connectSlotsByName(Change_database)

    def retranslateUi(self, Change_database):
        _translate = QtCore.QCoreApplication.translate
        Change_database.setWindowTitle(_translate("Change_database", "?????????????????? ????????????"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Change_database", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Change_database", "???????????????? ??????????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Change_database", "????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Change_database", "??????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Change_database", "?????????????? ?????????????? ????????????????????????????????, ???? (200????)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Change_database", "???????????? ???????????? ?????? ????????????????, ???? (150????)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Change_database", "??????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Change_database", "?????????????? ????????????????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Change_database", "??????????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Change_database", "?????????????? ????????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Change_database", "?????????? ??????????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Change_database", "?????????? ????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Change_database", "?????????? ????????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Change_database", "?????????? ??????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Change_database", "???????????????? ????????????????????????????????, ???? (200????)"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Change_database", "??????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Change_database", "?????? ????????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Change_database", "??????????????, ???? (200????)"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Change_database", "???????????????????? ??????????????, ???? (450????)"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Change_database", "?????????? ??????????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("Change_database", "?????????? ????????????????????????, ???? (1000????)"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("Change_database", "?????????? ??????????????????, ???? (200????)"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("Change_database", "????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("Change_database", "??????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("Change_database", "???????? ??????????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("Change_database", "???????? (??????????????, ????????????????, ????????????), ????"))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("Change_database", "?????????????? ????????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("Change_database", "???????????? ????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("Change_database", "???????????? ??????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(29)
        item.setText(_translate("Change_database", "???????????? ????????????????????????????????, ???? (200????)"))
        item = self.tableWidget.horizontalHeaderItem(30)
        item.setText(_translate("Change_database", "?????????? ????????????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(31)
        item.setText(_translate("Change_database", "????????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(32)
        item.setText(_translate("Change_database", "??????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(33)
        item.setText(_translate("Change_database", "????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(34)
        item.setText(_translate("Change_database", "??????????, ???? (500????)"))
        item = self.tableWidget.horizontalHeaderItem(35)
        item.setText(_translate("Change_database", "????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(36)
        item.setText(_translate("Change_database", "??????????????, ???? (250????)"))
        item = self.tableWidget.horizontalHeaderItem(37)
        item.setText(_translate("Change_database", "?????? ???????????? ????????????????????, ???? (200????)"))
        item = self.tableWidget.horizontalHeaderItem(38)
        item.setText(_translate("Change_database", "?????? ??????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(39)
        item.setText(_translate("Change_database", "????????????, ???? (200????)"))
        item = self.tableWidget.horizontalHeaderItem(40)
        item.setText(_translate("Change_database", "????????????, ????"))
        item = self.tableWidget.horizontalHeaderItem(41)
        item.setText(_translate("Change_database", "???????? ??????????????, ???? (10????)"))
        self.save_button.setToolTip(_translate("Change_database", "<html><head/><body><p>??????????????????</p></body></html>"))
        self.exit_button.setToolTip(_translate("Change_database", "??????????"))
