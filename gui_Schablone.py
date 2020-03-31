from PyQt5 import QtCore, QtGui, QtWidgets
import QT_Schablone as mw
import Schablone



class gui_Schablone:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.schablone: Schablone.Schablone = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

    def show(self, schablone: Schablone.Schablone):
        self.ui.lineEdit_Bezeichung.setText(schablone.Name)
        self.schablone = schablone

        self.Dialog.show()
        self.Dialog.exec()

    def accepted(self):
        self.schablone.Name = self.ui.lineEdit_Bezeichung.text()
        pass

    def rejected(self):

        pass