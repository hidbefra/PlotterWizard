from PyQt5 import QtCore, QtGui, QtWidgets
import os #Used in Testing Script

os.system("\"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\pyuic5.exe\" -x -o QT_MainWindow_schnittomat.py QT_MainWindow_schnittomat.ui") # gui übersetzten



import sys
import QT_MainWindow_schnittomat as mw


import gui_Arbeitsschrit
import gui_Schablone
import gui_Prozess


class gui_MainWindow_schnittomat:


    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.pushButton_Arbeitsschritt_hinzufgen.clicked.connect(self.pushButton_Arbeitsschritt_hinzufgen)
        self.ui.pushButton_Schablone_hinzufgen.clicked.connect(self.pushButton_Schablone_hinzufgen)
        self.ui.pushButton_Prozess_hinzufgen.clicked.connect(self.pushButton_Prozess_hinzufgen)

        self.Arbeitsschrit = gui_Arbeitsschrit.gui_Arbeitsschrit()
        self.Schablone = gui_Schablone.gui_Schablone()
        self.Prozess =  gui_Prozess.gui_Prozess()


    def show(self):
        self.MainWindow.show()

    def pushButton_Arbeitsschritt_hinzufgen(self):
        self.Arbeitsschrit.show()

    def pushButton_Schablone_hinzufgen(self):
        self.Schablone.show()

    def pushButton_Prozess_hinzufgen(self):
        self.Prozess.show()
