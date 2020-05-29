from PyQt5 import QtCore, QtGui, QtWidgets
import QT_Settings as mw
import copy

import model_Settings
import my_Json
import json


class gui_Settings():

    def __init__(self, parent, settings: model_Settings.Settings):
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.settings = settings

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.RestoreDefaults).clicked.connect(self.restore_default)

    def show(self):
        self.update_gui()

        self.Dialog.show()
        self.Dialog.exec()

    def update_gui(self):
        self.ui.textEdit_settings.setText(my_Json.dumps(self.settings.setings))
        self

    def accepted(self):
        try:
            self.settings.setings = my_Json.loads(self.ui.textEdit_settings.toPlainText())
            self.settings.safe_settings()
        except ValueError:
            print("ungültige Settings")

        pass

    def rejected(self):
        pass

    def restore_default(self):
        self.settings.restore_default()
        self.update_gui()