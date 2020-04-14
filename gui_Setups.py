from PyQt5 import QtCore, QtGui, QtWidgets
import model_Setups
from file_handling import FileHandling
import copy


import QT_Setups as mw



class gui_Setups(FileHandling):

    def __init__(self, parent):
        FileHandling.__init__(self, ".set")
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.setups: model_Setups.Setups = None
        self.new_setups: model_Setups.Setups = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)
        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)

    # def show(self, setups: model_Setups.Setups):
    #     self.ui.lineEdit_bezeichung.setText(setups.name)
    #     self.Setups = setups
    #
    #     self.Dialog.show()
    #     self.Dialog.exec()
    #
    # def accepted(self):
    #     self.Setups.name = self.ui.lineEdit_bezeichung.text()
    #
    # def rejected(self):
    #     pass

    def show(self, setups: model_Setups.Setups):
        self.setups = setups
        self.new_setups = copy.deepcopy(setups)

        self.update_gui()

        self.Dialog.show()
        self.Dialog.exec()

    def pushButton_Laden(self):
        data = self.open_file()
        if data is not None:
            self.new_setups.__init__(**data)
        self.update_gui()

    def pushButton_exportieren(self):
        self.update_model()
        self.safe_file(self.new_setups, self.new_setups.name)

    def accepted(self):
        self.update_model()
        self.setups.__dict__.update(self.new_setups.__dict__)

    def rejected(self):
        pass

    def update_model(self):
        self.new_setups.name = self.ui.lineEdit_bezeichung.text()

    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.new_setups.name)