import gui_MainWindow_schnittomat

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ui_translate


ui_translate.ui_translate() # zum übersetzten der gui's aus QT übersetzten

app = QtWidgets.QApplication(sys.argv)

MainWindow_schnittomat = gui_MainWindow_schnittomat.gui_MainWindow_schnittomat()
MainWindow_schnittomat.show()

sys.exit(app.exec_())
