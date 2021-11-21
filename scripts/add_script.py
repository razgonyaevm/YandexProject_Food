import sqlite3
import os
from PyQt5.QtWidgets import QMainWindow
from design_python.add_python import Ui_Add_database


class Add(QMainWindow, Ui_Add_database):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('other_files/Pirgoroy.db')  # подключаем базу данных
        self.show()
        # отслеживаем нажатия кнопок
        self.ok_button.clicked.connect(self.ok)
        self.pushButton.clicked.connect(self.ex)

    def ok(self):
        """функция для записи нового элемента, который добавляет пользователь"""
        system = self.lineEdit.text()
        ind = system.index(' ')
        system = [system[:ind], system[ind + 1:]]
        # работаем с файлом id.txt (увеличиваем index, который лежит в файле)
        if len(system) != 0:
            with open('other_files/id.txt') as file:
                a = int(file.readline())
                a += 1
            os.system(r' >other_files/id.txt')
            with open('other_files/id.txt', 'w') as file:
                file.write(str(a))

        cur = self.con.cursor()
        try:  # работаем с таблицами базы данных
            cur.execute("INSERT INTO Menu (id, Type, Name) VALUES (?, ?, ?)", (a, system[0], system[1]))
            cur.execute("INSERT INTO Ordering (id, Name, Choose) VALUES (?, ?, ?)", (a, system[1], 0))
            cur.execute("INSERT INTO Recipy (id, 'Название блюда', 'Бананы, гр', "
                        "'Ветчина, гр', 'Горошек зеленый консервированный, уп (200гр)',"
                        "'Зелень укропа или петрушки, уп (150гр)', 'Кабачок, гр',"
                        "'Капуста белокочанная, гр', 'Картофель, гр',"
                        "'Колбаса копченая, гр', 'Крупа гречневая, уп (500гр)',"
                        "'Крупа манная, уп (500гр)', 'Крупа перловая, уп (500гр)',"
                        "'Крупа рисовая, уп (500гр)',"
                        "'Кукуруза консервированная, уп (200гр)',"
                        "'Лимон, гр',"
                        "'Лук репчатый, гр', 'Майонез, уп (200мл)', 'Макаронные изделия, уп (450гр)',"
                        "'Масло оливковое, уп (500мл)', 'Масло растительное, уп (1000мл)',"
                        "'Масло сливочное, уп (200гр)', 'Молоко, уп (500мл)', 'Морковь, гр',"
                        "'Мука пшеничная, уп (500гр)', 'Мясо (свинина, говядина, курица), гр',"
                        "'Овсяные хлопья, уп (500гр)', 'Огурцы свежие, гр',"
                        "'Огурцы соленые, гр', 'Оливки консервированные, уп (200гр)',"
                        "'Перец болгарский, гр', 'Помидоры, гр', 'Пшено, уп (500гр)',"
                        "'Рыба, гр', 'Сахар, уп (500гр)', 'Свекла, гр',"
                        "'Сметана, уп (250мл)', 'Сыр мягкий рассольный, уп (200гр)',"
                        "'Сыр твердый, гр', 'Творог, уп (200гр)', 'Яблоки, гр',"
                        "'Яйцо куриное, уп (10шт)') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
                        "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                        "?, ?)", (a, system[1], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        except IndexError:
            pass
        except UnboundLocalError:
            pass
        self.con.commit()
        self.label_2.setText('Готово!')

    def ex(self):
        """функция выхода"""
        self.close()
