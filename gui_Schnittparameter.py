from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import QT_Schnittparameter as mw
import model_Schnittparameter
import my_Json



class gui_Schnittparameter:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.schnittparameter: model_Schnittparameter.Schnittparameter = None
        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)
        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)

    def show(self, schnittparameter: model_Schnittparameter.Schnittparameter):
        self.schnittparameter = schnittparameter
        self.ui.lineEdit_bezeichung.setText(self.schnittparameter.name)
        self.Dialog.show()
        self.Dialog.exec()
        return self.schnittparameter

    def pushButton_exportieren(self):
        self.update_model()

        f = open(f"Setups\\{self.schnittparameter.name}.cut", "w+")
        f.write(my_Json.dumps(self.schnittparameter))
        f.close()

    def pushButton_Laden(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        # dlg.setFilter("Text files (*.txt)")
        # filenames = QStringList()

        if dlg.exec_():
            filenames = dlg.selectedFiles()

            f = open(filenames[0], "r")
            self.schnittparameter = my_Json.loads(f.read(), model_Schnittparameter.Schnittparameter)
            f.close()

        self.update_gui()

    def update_model(self):
        self.schnittparameter.name = self.ui.lineEdit_bezeichung.text()

    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.schnittparameter.name)