from PyQt5 import QtCore, QtGui, QtWidgets
import os #Used in Testing Script

os.system("\"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\pyuic5.exe\" -x -o QT_Schablone.py QT_Schablone.ui") # gui übersetzten



import sys
import QT_Schablone as mw



class gui_Schablone:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)


    def show(self):
        self.Dialog.show()