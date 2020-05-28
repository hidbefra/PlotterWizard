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
        self.ui.pushButton_Geometrie_Importieren.clicked.connect(self.pushButton_Geometrie_Importieren)

    def show(self, arbeitsschritt: model_Arbeitsschritt.Arbeitsschritt):
        self.arbeitsschritt = arbeitsschritt
        self.new_arbeitsschritt = copy.deepcopy(arbeitsschritt)

        self.update_gui()

        self.Dialog.show()
        self.Dialog.exec()

    def pushButton_Schnittparameter(self):
        self.update_model()
        self.new_arbeitsschritt.schnittparameter_decode()
        self.guischnittparameter.show(self.new_arbeitsschritt.schnittparameter)
        self.ui.checkBox_extract_parameter.setChecked(not self.new_arbeitsschritt.schnittparameter.custom_schnittparameter)


    def accepted(self):
        self.update_model()
        # self.arbeitsschritt.__dict__.update(self.new_arbeitsschritt.__dict__)
        self.arbeitsschritt.copy_from(self.new_arbeitsschritt)

        if not self.ui.checkBox_extract_parameter.isChecked():
            self.new_arbeitsschritt.assigned_new_schnittparameter()
        pass

    def rejected(self):
        pass

    def pushButton_exportieren(self):
        self.update_model()
        self.export_file(self.new_arbeitsschritt, self.new_arbeitsschritt.name)

    def pushButton_Laden(self):
        data = self.import_file()
        if data is not None:
            self.new_arbeitsschritt.__init__(**data)
        self.update_gui()

    def update_model(self):
        self.new_arbeitsschritt.name = self.ui.lineEdit_bezeichung.text()
        self.new_arbeitsschritt.hpgl_structure.code = self.ui.textBrowser_Geometrie.toPlainText()
        self.new_arbeitsschritt.schnittparameter.custom_schnittparameter = \
            0 if self.ui.checkBox_extract_parameter.isChecked() is True else 1

        data = self.ui.textBrowser_Geometrie.toPlainText()
        self.new_arbeitsschritt.hpgl_structure.decode(data)

        self.new_arbeitsschritt.offset.dx = self.ui.doubleSpinBox_offset_x.value()
        self.new_arbeitsschritt.offset.dy = self.ui.doubleSpinBox_offset_y.value()
        self.new_arbeitsschritt.offset.phi = self.ui.doubleSpinBox_offset_phi.value()


    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.new_arbeitsschritt.name)
        self.ui.textBrowser_Geometrie.setText(self.new_arbeitsschritt.hpgl_structure.encode())
        self.ui.checkBox_extract_parameter.setChecked(not self.new_arbeitsschritt.schnittparameter.custom_schnittparameter)

        self.ui.doubleSpinBox_offset_x.setValue(self.new_arbeitsschritt.offset.dx)
        self.ui.doubleSpinBox_offset_y.setValue(self.new_arbeitsschritt.offset.dy)
        self.ui.doubleSpinBox_offset_phi.setValue(self.new_arbeitsschritt.offset.phi)

    def pushButton_Geometrie_Importieren(self):
        data = self.open_with_file_dialog()
        if data is not None:
            # self.new_arbeitsschritt.hpgl_structure.code = data
            self.new_arbeitsschritt.hpgl_structure.decode(data)
            self.update_gui()
