import sqlite3
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from design_python.make_python import Ui_Make_an_order


class Order(QMainWindow, Ui_Make_an_order):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('../Pirgoroy.db')

        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM Ordering").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

        self.tableWidget.itemChanged.connect(self.item_changed)
        self.make_button.clicked.connect(self.save_results)

        self.show()

    def save_results(self):
        cur = self.con.cursor()
        result = cur.execute("""SELECT name, choose FROM Ordering
                WHERE cast(choose as integer) > 0;""").fetchall()
        os.system(r' >../order.txt')
        with open('../order.txt', 'w') as order:
            ans = []
            for i in result:
                order.write(f'{i[0]} {i[1]}шт\n')
                ans.append(f'{i[0]} {i[1]}шт\n')
        m = ''
        for i, k in result:
            m += i + ' ' + str(k) + '\n'
        self.textEdit.setText(m)
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE Ordering SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            print(que)
            cur.execute(que)
            self.con.commit()
            self.modified.clear()


    def item_changed(self, item):
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        self.modified[self.titles[item.column()]] = item.text()


