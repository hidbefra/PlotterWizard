# install PyQt5
# install PyQt5-tool

from PyQt5 import QtCore, QtGui, QtWidgets
import os #Used in Testing Script

os.system("\"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\pyuic5.exe\" -x -o MainWindow_schnittomat.py MainWindow_schnittomat.ui") # gui übersetzten



import sys
import MainWindow_schnittomat as mw



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mw.Ui_MainWindow()

ui.setupUi(MainWindow)


MainWindow.show()
sys.exit(app.exec_())


