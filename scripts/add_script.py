import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from design_python.add_python import Ui_Add_database


class Add(QMainWindow, Ui_Add_database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('../other_files/Pirgoroy.db')

        self.show()