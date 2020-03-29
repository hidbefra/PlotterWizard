from PyQt5 import QtCore, QtGui, QtWidgets
import Prozess


import QT_Prozess as mw



class gui_Prozess:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)


    def show(self, prozess: Prozess.Prozess):
        self.ui.lineEdit_bezeichung.setText(prozess.Name)
        self.Dialog.show()