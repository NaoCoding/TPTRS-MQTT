from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import _lang , _userSetting

class start_screen(QMainWindow, _lang.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    
    gui = QtWidgets.QApplication(sys.argv)
    window = start_screen()
    window.show()
    sys.exit(gui.exec_())