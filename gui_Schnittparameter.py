from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import QT_Schnittparameter as mw
import model_Schnittparameter
import my_Json
from file_handling import FileHandling



class gui_Schnittparameter(FileHandling):

    def __init__(self, parent):
        FileHandling.__init__(self, ".cut")
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.schnittparameter: model_Schnittparameter.Schnittparameter = None
        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)
        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)
        self.ui.buttonBox.accepted.connect(self.accepted)


    def show(self, schnittparameter: model_Schnittparameter.Schnittparameter):
        self.schnittparameter = schnittparameter
        self.ui.lineEdit_bezeichung.setText(self.schnittparameter.name)
        self.Dialog.show()
        self.Dialog.exec()
        # return self.schnittparameter

    def accepted(self):
        self.update_model()

    def pushButton_exportieren(self):
        self.update_model()
        self.safe_file(self.schnittparameter,self.schnittparameter.name)

    def pushButton_Laden(self):
        data = self.open_file()
        print (data)
        if data is not None:
            self.schnittparameter.__init__(**data)
        self.update_gui()

    def update_model(self):
        self.schnittparameter.name = self.ui.lineEdit_bezeichung.text()

    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.schnittparameter.name)