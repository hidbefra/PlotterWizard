from PyQt5 import QtCore, QtGui, QtWidgets
import QT_Settings as mw
import copy
from file_handling import FileHandling
import model_Settings
import my_Json


class gui_Settings(FileHandling):

    def __init__(self, parent, settings: model_Settings.Settings):
        FileHandling.__init__(self, ".shb")
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.settings = settings


    def show(self):

        self.update_gui()

        self.Dialog.show()
        self.Dialog.exec()


    def update_gui(self):
        self.ui.textEdit_settings.setText(my_Json.dumps(self.settings))
        self