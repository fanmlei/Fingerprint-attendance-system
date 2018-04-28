from PyQt5.QtWidgets import *
from MainWindow import MainWindow
from login import Login

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    if login.exec_() == QDialog.Accepted:
         main = MainWindow(login.id)
         main.show()
    sys.exit(app.exec_())
