from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import QT_Schnittparameter as mw
import model_Schnittparameter
import my_Json
from file_handling import FileHandling
import copy



class gui_Schnittparameter(FileHandling):

    def __init__(self, parent):
        FileHandling.__init__(self, ".cut")
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.schnittparameter: model_Schnittparameter.Schnittparameter = None
        self.new_schnittparameter: model_Schnittparameter.Schnittparameter = None

        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)
        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)
        self.ui.buttonBox.accepted.connect(self.accepted)


    def show(self, schnittparameter: model_Schnittparameter.Schnittparameter):
        self.schnittparameter = schnittparameter
        self.new_schnittparameter = copy.deepcopy(schnittparameter)

        self.update_gui()

        self.Dialog.show()
        self.Dialog.exec()
        # return self.schnittparameter

    def accepted(self):
        self.update_model()
        # self.schnittparameter.__dict__.update(self.new_schnittparameter.__dict__)
        self.schnittparameter.copy_from(self.new_schnittparameter)

    def pushButton_exportieren(self):
        self.update_model()
        self.safe_json_file(self.new_schnittparameter, self.new_schnittparameter.name)

    def pushButton_Laden(self):
        data = self.open_json_file()
        print (data)
        if data is not None:
            self.new_schnittparameter.__init__(**data)
        self.update_gui()

    def update_model(self):
        self.new_schnittparameter.name = self.ui.lineEdit_bezeichung.text()

        self.new_schnittparameter.parameter_dict["LL"].set_parameter([self.ui.doubleSpinBox_LL.value()])
        self.new_schnittparameter.parameter_dict["ML"].set_parameter([self.ui.doubleSpinBox_ML.value()])
        self.new_schnittparameter.parameter_dict["LF"].set_parameter([self.ui.spinBox_LF.value()])
        self.new_schnittparameter.parameter_dict["VS"].set_parameter([self.ui.doubleSpinBox_VS.value()])
        self.new_schnittparameter.parameter_dict["VU"].set_parameter([self.ui.doubleSpinBox_VU.value()])
        self.new_schnittparameter.parameter_dict["QU"].set_parameter([self.ui.spinBox_QU.value()])

        self.new_schnittparameter.parameter_dict["AS"].set_parameter([self.ui.spinBox_AS_PD.value(),
                                                                      self.ui.spinBox_AS_PU.value()])

        self.new_schnittparameter.parameter_dict["PB2"].set_parameter([1 if self.ui.checkBox_PB2.isChecked() is True else 0])
        self.new_schnittparameter.parameter_dict["PB4"].set_parameter([1 if self.ui.checkBox_PB4.isChecked() is True else 0])
        self.new_schnittparameter.parameter_dict["EG"].set_parameter([1 if self.ui.checkBox_EG.isChecked() is True else 0])

        self.new_schnittparameter.parameter_dict["XX13,3"].set_parameter([self.ui.comboBox_XX13_3.currentIndex()])

    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.new_schnittparameter.name)

        self.ui.doubleSpinBox_LL.setValue(self.new_schnittparameter.parameter_dict["LL"].get_parameters()[0])
        self.ui.doubleSpinBox_ML.setValue(self.new_schnittparameter.parameter_dict["ML"].get_parameters()[0])
        self.ui.spinBox_LF.setValue(self.new_schnittparameter.parameter_dict["LF"].get_parameters()[0])
        self.ui.doubleSpinBox_VS.setValue(self.new_schnittparameter.parameter_dict["VS"].get_parameters()[0])
        self.ui.doubleSpinBox_VU.setValue(self.new_schnittparameter.parameter_dict["VU"].get_parameters()[0])
        self.ui.spinBox_QU.setValue(self.new_schnittparameter.parameter_dict["QU"].get_parameters()[0])

        self.ui.spinBox_AS_PD.setValue(self.new_schnittparameter.parameter_dict["AS"].get_parameters()[0])
        self.ui.spinBox_AS_PU.setValue(self.new_schnittparameter.parameter_dict["AS"].get_parameters()[1])

        self.ui.checkBox_PB2.setChecked(self.new_schnittparameter.parameter_dict["PB2"].get_parameters()[0])
        self.ui.checkBox_PB4.setChecked(self.new_schnittparameter.parameter_dict["PB4"].get_parameters()[0])
        self.ui.checkBox_EG.setChecked(self.new_schnittparameter.parameter_dict["EG"].get_parameters()[0])

        self.ui.comboBox_XX13_3.setCurrentIndex(self.new_schnittparameter.parameter_dict["XX13,3"].get_parameters()[1])


