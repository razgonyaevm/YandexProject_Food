import sqlite3
import os

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from design_python.make_python import Ui_Make_an_order


class Order(QMainWindow, Ui_Make_an_order):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('other_files/Pirgoroy.db')  # подключаем базу данных Pirgoroy

        # запсь значений в таблицу в форме
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Ordering").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

        self.show()

        # отслеживание изменений, которые внес пользователь
        self.tableWidget.itemChanged.connect(self.item_changed)

        # отслеживание нажатий кнопок
        self.exit_button.clicked.connect(self.ex)
        self.make_button.clicked.connect(self.save_results)

    def save_results(self):
        """функция для обновления таблицы Ordering и записи в файл order.txt"""
        if self.modified:
            cur = self.con.cursor()
            for i in self.modified.keys():
                que = "UPDATE Ordering SET\n"
                que += i[0] + '=' + self.modified[i]
                que += f'\nWHERE id='
                que += str(i[1])
                cur.execute(que)
                self.con.commit()
            self.modified.clear()

        cur = self.con.cursor()
        result = cur.execute("""SELECT name, choose FROM Ordering
                WHERE Choose > 0;""").fetchall()
        os.system(r' >other_files/order.txt')
        with open('other_files/order.txt', 'w') as order:
            for i in result:
                order.write(f'{i[0]} {i[1]}шт\n')
        m = ''
        for i, k in result:
            m += i + ' ' + str(k) + '\n'
        self.textEdit.setText(m)

    def item_changed(self, item):
        """функция отслеживания обновлений таблицы"""
        self.modified[self.titles[item.column()], item.row() + 1] = item.text()

    def ex(self):
        """функция выхода"""
        self.close()
