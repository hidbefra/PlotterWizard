from PyQt5 import QtCore, QtGui, QtWidgets

import QT_Arbeitsschritt as mw
import gui_Schnittparameter
import Arbeitsschritt


class gui_Arbeitsschrit:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        self.ui.pushButton_Schnittparameter.clicked.connect(self.pushButton_Schnittparameter)

        self.schnittparameter = gui_Schnittparameter.gui_Schnittparameter()


    def show(self, arbeitsschrit: Arbeitsschritt.Arbeitsschritt):
        self.ui.lineEdit_bezeichung.setText(arbeitsschrit.Name)
        self.Dialog.show()

    def pushButton_Schnittparameter(self):
        self.schnittparameter.show()
