import sqlite3
import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from design_python.del_python import Ui_Remove_database
from scripts.make_order_script import Order


class Remove(QMainWindow, Ui_Remove_database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('../other_files/Pirgoroy.db')  #
        self.upd()
        self.show()

        #
        self.update_button.clicked.connect(self.upd)
        self.delete_button.clicked.connect(self.remove)
        self.exit_button.clicked.connect(self.cl)

    def remove(self):
        """функция для удаления элементов из таблиц Menu, Ordering, Recipy"""
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            with open('../other_files/id.txt') as file:
                a = int(file.readline())
                while True:
                    if str(a) in ids:
                        a -= 1
                    else:
                        break

            os.system(r' >../other_files/id.txt')
            os.system(r' >../shopping_list.txt')
            with open('../other_files/id.txt', 'w') as file:
                file.write(str(a))
            cur = self.con.cursor()
            cur.execute("DELETE FROM Menu WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            cur.execute("DELETE FROM Ordering WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            cur.execute("DELETE FROM Recipy WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.con.commit()
            a = Order()
            a.save_results()

    def upd(self):
        """функция обновления таблицы в форме"""
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Menu").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def cl(self):
        """функция закрытия"""
        self.close()
