import sqlite3
import os
from PyQt5.QtWidgets import QMainWindow
from design_python.add_python import Ui_Add_database


class Add(QMainWindow, Ui_Add_database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('../other_files/Pirgoroy.db')
        self.show()

        self.ok_button.clicked.connect(self.ok)
        self.pushButton.clicked.connect(self.ex)

    def ok(self):
        system = self.lineEdit.text()
        ind = system.index(' ')
        system = [system[:ind], system[ind + 1:]]

        if len(system) != 0:
            with open('../other_files/id.txt') as file:
                a = int(file.readline())
                a += 1
            os.system(r' >../other_files/id.txt')
            with open('../other_files/id.txt', 'w') as file:
                file.write(str(a))

        cur = self.con.cursor()
        try:
            cur.execute("INSERT INTO Menu (id, Type, Name) VALUES (?, ?, ?)", (a, system[0], system[1])).fetchall()
            cur.execute("INSERT INTO Ordering (id, Name, Choose) VALUES (?, ?, ?)", (a, system[1], 0)).fetchall()
        except IndexError:
            pass
        except UnboundLocalError:
            pass
        self.con.commit()
        self.label_2.setText('Готово!')

    def ex(self):
        self.close()

