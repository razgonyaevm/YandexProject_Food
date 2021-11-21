import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from design_python.hello_python import Ui_Hello_Window
from scripts.make_order_script import Order
from scripts.remove_script import Remove
from scripts.add_script import Add
from scripts.change_script import Change
from scripts.itog_script import Itog


class Hello(QMainWindow, Ui_Hello_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # отслеживаем нажатия кнопки
        self.exit_button.clicked.connect(self.exit)
        self.make_order.clicked.connect(self.make)
        self.remove.clicked.connect(self.rem)
        self.add.clicked.connect(self.ad)
        self.change.clicked.connect(self.chan)
        self.pushButton.clicked.connect(self.it)
        try:  # этот блок нужен для установки иконки приложения
            from PyQt5.QtWinExtras import QtWin
            myappid = 'mycompany.myproduct.subproduct.version'
            QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
        except ImportError:
            pass

    def exit(self):
        self.close()  # закрывает приветственную форму

    def ad(self):
        self.d = Add()  # открывает форму добавления элементов

    def make(self):
        self.mk = Order()  # открывает форму заказа

    def rem(self):
        self.rm = Remove()  # открывает форму удаления элементов

    def chan(self):
        self.ch = Change()  # открывавет форму изменения базы данных

    def it(self):
        self.ito = Itog()  # открывает форму итогового заполнения списка покупок


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/cake_icon.png'))
    ex = Hello()
    ex.setWindowIcon(QIcon('../images/cake_icon.png'))
    ex.show()
    sys.exit(app.exec_())
