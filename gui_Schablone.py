from PyQt5 import QtCore, QtGui, QtWidgets
import QT_Schablone as mw
import model_Schablone



class gui_Schablone:

    def __init__(self, parent):
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.schablone: model_Schablone.Schablone = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

    def show(self, schablone: model_Schablone.Schablone):
        self.ui.lineEdit_Bezeichung.setText(schablone.name)
        self.schablone = schablone

        self.Dialog.show()
        self.Dialog.exec()

    def accepted(self):
        self.schablone.name = self.ui.lineEdit_Bezeichung.text()
        pass

    def rejected(self):

        pass