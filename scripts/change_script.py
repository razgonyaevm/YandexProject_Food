import sqlite3

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from design_python.change_python import Ui_Change_database


class Change(QMainWindow, Ui_Change_database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('other_files/Pirgoroy.db')  # подключаем базу данных Pirgoroy
        self.con.row_factory = sqlite3.Row
        self.update()

        self.show()
        # отслеживаем нажатия кнопок
        self.exit_button.clicked.connect(self.ex)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.save_button.clicked.connect(self.save)

    def ex(self):
        self.close()  # закрываем форму

    def save(self):  # записываем изменения в таблицу Recipy
        valid = QMessageBox.question(
            self, '', "Дейтвительно сохранить?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            if self.modified:
                cur = self.con.cursor()
                for i in self.modified.keys():
                    que = "UPDATE Recipy SET\n"
                    que += f"'{i[0]}'" + '=' + self.modified[i]
                    que += f'\nWHERE id='
                    que += str(i[1])
                    cur.execute(que)
                    self.con.commit()
                self.modified.clear()
                self.update()

    def item_changed(self, item):  # записываем изменения в self.modified
        self.modified[self.titles[item.column()], item.row() + 1] = item.text()

    def update(self):  # обновляем таблицу в форме значениями из таблицы Recipy
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Recipy").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}
