# install PyQt5
# install PyQt5-tool

from PyQt5 import QtCore, QtGui, QtWidgets
import os #Used in Testing Script

os.system("\"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\pyuic5.exe\" -x -o MainWindow.py MainWindow.ui") # gui übersetzten

import sys
import MainWindow as mw


def say_hello():

    print("Button clicked, Hello!")
    ui.label.setText("blob")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mw.Ui_MainWindow()

ui.setupUi(MainWindow)

ui.pushButton.clicked.connect(say_hello)

MainWindow.show()
ui.label.setText("hallo123")
sys.exit(app.exec_())




