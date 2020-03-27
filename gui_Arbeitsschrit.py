from PyQt5 import QtCore, QtGui, QtWidgets
import os #Used in Testing Script

os.system("\"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\pyuic5.exe\" -x -o QT_Arbeitsschrit.py QT_Arbeitsschrit.ui") # gui übersetzten



import sys
import QT_Arbeitsschrit as mw
import gui_Schnittparameter



class gui_Arbeitsschrit:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        self.ui.pushButton_Schnittparameter.clicked.connect(self.pushButton_Schnittparameter)

        self.schnittparameter = gui_Schnittparameter.gui_Schnittparameter()


    def show(self):
        self.Dialog.show()

    def pushButton_Schnittparameter(self):
        self.schnittparameter.show()
