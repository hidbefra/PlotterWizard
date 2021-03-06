from PyQt5 import QtCore, QtGui, QtWidgets
import QT_Schablone as mw
import model_Schablone
import copy
from file_handling import FileHandling



class gui_Schablone(FileHandling):

    def __init__(self, parent):
        FileHandling.__init__(self, ".shb")
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.schablone: model_Schablone.Schablone = None
        self.new_schablone: model_Schablone.Schablone = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)
        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)

        self.Dialog.setFixedSize(self.Dialog.sizeHint())

    # def show(self, schablone: model_Schablone.Schablone):
    #     self.ui.lineEdit_Bezeichung.setText(schablone.name)
    #     self.schablone = schablone
    #
    #     self.Dialog.show()
    #     self.Dialog.exec()
    #
    # def accepted(self):
    #     self.schablone.name = self.ui.lineEdit_Bezeichung.text()
    #     pass
    #
    # def rejected(self):
    #
    #     pass


    def show(self, schablone: model_Schablone.Schablone):
        self.schablone = schablone
        self.new_schablone = copy.deepcopy(schablone)

        self.update_gui()

        self.Dialog.show()
        self.Dialog.exec()


    def pushButton_Laden(self):
        data = self.import_file()
        if data is not None:
            self.new_schablone.__init__(**data)
        self.update_gui()


    def pushButton_exportieren(self):
        self.update_model()
        self.export_file(self.new_schablone, self.new_schablone.name)


    def accepted(self):
        self.update_model()
        self.schablone.copy_from(self.new_schablone)
        # self.schablone.__dict__.update(self.new_schablone.__dict__)

    def rejected(self):
        pass


    def update_model(self):
        self.new_schablone.name = self.ui.lineEdit_bezeichung.text()

        self.new_schablone.offset.dx = self.ui.doubleSpinBox_offset_x.value()
        self.new_schablone.offset.dy = self.ui.doubleSpinBox_offset_y.value()
        self.new_schablone.offset.phi = self.ui.doubleSpinBox_offset_phi.value()


    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.new_schablone.name)

        self.ui.doubleSpinBox_offset_x.setValue(self.new_schablone.offset.dx)
        self.ui.doubleSpinBox_offset_y.setValue(self.new_schablone.offset.dy)
        self.ui.doubleSpinBox_offset_phi.setValue(self.new_schablone.offset.phi)
