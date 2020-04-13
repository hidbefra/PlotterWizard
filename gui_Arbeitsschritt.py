from PyQt5 import QtCore, QtGui, QtWidgets

import QT_Arbeitsschritt as mw
import gui_Schnittparameter
import model_Arbeitsschritt
import my_Json
from file_handling import FileHandling

import copy


class gui_Arbeitsschrit(FileHandling):

    def __init__(self, parent):
        FileHandling.__init__(self,".wst")
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)

        self.new_arbeitsschritt: model_Arbeitsschritt.Arbeitsschritt = None
        self.arbeitsschritt: model_Arbeitsschritt.Arbeitsschritt = None
        self.guischnittparameter = gui_Schnittparameter.gui_Schnittparameter(self.Dialog)

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)
        self.ui.pushButton_Schnittparameter.clicked.connect(self.pushButton_Schnittparameter)
        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)
        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)

    def show(self, arbeitsschritt: model_Arbeitsschritt.Arbeitsschritt):
        self.ui.lineEdit_bezeichung.setText(arbeitsschritt.name)
        self.arbeitsschritt = arbeitsschritt
        self.new_arbeitsschritt = copy.deepcopy(arbeitsschritt)

        self.Dialog.show()
        self.Dialog.exec()

    def pushButton_Schnittparameter(self):
        self.guischnittparameter.show(self.new_arbeitsschritt.schnittparameter)

    def accepted(self):
        self.update_model()
        self.arbeitsschritt.__dict__.update(self.new_arbeitsschritt.__dict__)
        pass

    def rejected(self):
        pass

    def pushButton_exportieren(self):
        self.update_model()
        self.safe_file(self.new_arbeitsschritt, self.new_arbeitsschritt.name)

    def pushButton_Laden(self):
        data = self.open_file()
        if data is not None:
            self.new_arbeitsschritt.__init__(**data)
        self.update_gui()

    def update_model(self):
        self.new_arbeitsschritt.name = self.ui.lineEdit_bezeichung.text()

    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.new_arbeitsschritt.name)