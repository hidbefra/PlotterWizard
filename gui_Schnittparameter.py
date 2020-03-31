from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import QT_Schnittparameter as mw



class gui_Schnittparameter:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)


    def show(self):
        self.Dialog.show()
        self.Dialog.exec()