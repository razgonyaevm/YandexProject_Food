import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from design_python.del_python import Ui_Remove_database


class Remove(QMainWindow, Ui_Remove_database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('../other_files/Pirgoroy.db')
        self.upd()
        self.show()

        self.update_button.clicked.connect(self.upd)
        self.delete_button.clicked.connect(self.remove)
        self.exit_button.clicked.connect(self.cl)

    def remove(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE FROM Menu WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.con.commit()

    def upd(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Menu").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def cl(self):
        self.close()

