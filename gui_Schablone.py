from PyQt5 import QtCore, QtGui, QtWidgets

import QT_Schablone as mw
import Schablone



class gui_Schablone:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)


    def show(self, schablone: Schablone.Schablone):
        self.ui.lineEdit_Bezeichung.setText(schablone.Name)
        self.Dialog.show()