from PyQt5 import QtCore, QtGui, QtWidgets

import QT_Arbeitsschritt as mw
import gui_Schnittparameter
import Arbeitsschritt


class gui_Arbeitsschrit:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.schnittparameter = gui_Schnittparameter.gui_Schnittparameter()
        self.arbeitsschritt: Arbeitsschritt.Arbeitsschritt = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)
        self.ui.pushButton_Schnittparameter.clicked.connect(self.pushButton_Schnittparameter)




    def show(self, arbeitsschritt: Arbeitsschritt.Arbeitsschritt):
        self.ui.lineEdit_bezeichung.setText(arbeitsschritt.Name)
        self.arbeitsschritt = arbeitsschritt

        self.Dialog.show()
        self.Dialog.exec()

    def pushButton_Schnittparameter(self):
        self.schnittparameter.show()

    def accepted(self):
        self.arbeitsschritt.Name = self.ui.lineEdit_bezeichung.text()
        pass

    def rejected(self):
        pass