import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import mainWindow

LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))



class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainWindow = Main()
    sys.exit(app.exec_())
