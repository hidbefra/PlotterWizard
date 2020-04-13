from PyQt5 import QtCore, QtGui, QtWidgets
import model_Setups


import QT_Setups as mw



class gui_Setups:

    def __init__(self, parent):
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Setups: model_Setups.Setups = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

    def show(self, setups: model_Setups.Setups):
        self.ui.lineEdit_bezeichung.setText(setups.name)
        self.Setups = setups

        self.Dialog.show()
        self.Dialog.exec()

    def accepted(self):
        self.Setups.name = self.ui.lineEdit_bezeichung.text()

    def rejected(self):
        pass