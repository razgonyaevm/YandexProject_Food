import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from design_python.hello_python import Ui_Hello_Window
from scripts.make_order_script import Order
from scripts.remove_script import Remove
from scripts.add_script import Add


class Hello(QMainWindow, Ui_Hello_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_button.clicked.connect(self.exit)
        self.make_order.clicked.connect(self.make)
        self.remove.clicked.connect(self.rem)
        self.add.clicked.connect(self.ad)
        try:
            from PyQt5.QtWinExtras import QtWin
            myappid = 'mycompany.myproduct.subproduct.version'
            QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
        except ImportError:
            pass

    def exit(self):
        self.close()

    def ad(self):
        self.close()
        self.d = Add()

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
