from PyQt5 import QtCore, QtGui, QtWidgets

import QT_Arbeitsschritt as mw
import gui_Schnittparameter
import model_Arbeitsschritt
import my_Json


class gui_Arbeitsschrit:

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.arbeitsschritt: model_Arbeitsschritt.Arbeitsschritt = None
        self.guischnittparameter = gui_Schnittparameter.gui_Schnittparameter()
        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)
        self.ui.pushButton_Schnittparameter.clicked.connect(self.pushButton_Schnittparameter)
        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)
        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)

    def show(self, arbeitsschritt: model_Arbeitsschritt.Arbeitsschritt):
        self.ui.lineEdit_bezeichung.setText(arbeitsschritt.name)
        self.arbeitsschritt = arbeitsschritt

        self.Dialog.show()
        self.Dialog.exec()
        return self.arbeitsschritt

    def pushButton_Schnittparameter(self):
        self.arbeitsschritt.schnittparameter = self.guischnittparameter.show(self.arbeitsschritt.schnittparameter)

    def accepted(self):
        self.arbeitsschritt.name = self.ui.lineEdit_bezeichung.text()
        pass

    def rejected(self):
        pass

    def pushButton_exportieren(self):
        self.update_model()
        parent = self.arbeitsschritt.parent
        self.arbeitsschritt.parent = None
        f = open(f"Setups\\{self.arbeitsschritt.name}.lab", "w+")
        f.write(my_Json.dumps(self.arbeitsschritt))
        f.close()
        self.arbeitsschritt.parent = parent

    def pushButton_Laden(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        # dlg.setFilter("Text files (*.txt)")
        # filenames = QStringList()

        if dlg.exec_():
            parent = self.arbeitsschritt.parent
            filenames = dlg.selectedFiles()

            f = open(filenames[0], "r")
            self.arbeitsschritt = my_Json.loads(f.read(), model_Arbeitsschritt.Arbeitsschritt)
            f.close()
            self.arbeitsschritt.parent = parent

        self.update_gui()

    def update_model(self):
        self.arbeitsschritt.name = self.ui.lineEdit_bezeichung.text()

    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.arbeitsschritt.name)