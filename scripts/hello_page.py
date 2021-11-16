import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from design_python.hello_python import Ui_Hello_Window
from design_python.del_python import Ui_Remove_database
from design_python.add_python import Ui_Add_database
from design_python.make_python import Ui_Make_an_order
from design_python.change_python import Ui_Change_database
from scripts.make_order_script import Order
from scripts.remove_script import Remove


class Hello(QMainWindow, Ui_Hello_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_button.clicked.connect(self.exit)
        self.make_order.clicked.connect(self.make)
        self.remove.clicked.connect(self.rem)
        try:
            # Включите в блок try/except, если вы также нацелены на Mac/Linux
            from PyQt5.QtWinExtras import QtWin  # !!!
            myappid = 'mycompany.myproduct.subproduct.version'  # !!!
            QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!
        except ImportError:
            pass

    def exit(self):
        self.close()

    def make(self):
        self.close()
        self.mk = Order()

    def rem(self):
        self.close()
        self.rm = Remove()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/cake_icon.png'))
    ex = Hello()
    ex.setWindowIcon(QIcon('../images/cake_icon.png'))
    ex.show()
    sys.exit(app.exec_())