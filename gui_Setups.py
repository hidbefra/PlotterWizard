from PyQt5 import QtCore, QtGui, QtWidgets
import Setups


import QT_Setups as mw



class gui_Setups:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Setups: Setups.Setups = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

    def show(self, setups: Setups.Setups):
        self.ui.lineEdit_bezeichung.setText(setups.Name)
        self.Setups = setups

        self.Dialog.show()
        self.Dialog.exec()

    def accepted(self):
        self.Setups.Name = self.ui.lineEdit_bezeichung.text()

    def rejected(self):
        pass