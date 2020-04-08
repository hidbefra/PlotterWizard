from PyQt5 import QtCore, QtGui, QtWidgets
import model_Prozess


import QT_Prozess as mw



class gui_Prozess:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.prozess: model_Prozess.Prozess = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)


    def show(self, prozess: model_Prozess.Prozess):
        self.ui.lineEdit_bezeichung.setText(prozess.name)
        self.prozess = prozess

        self.Dialog.show()
        self.Dialog.exec()


    def accepted(self):
        self.prozess.name = self.ui.lineEdit_bezeichung.text()

    def rejected(self):
        pass