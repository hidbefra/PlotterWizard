# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Schablone.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 563)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 530, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.lineEdit_Bezeichung = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Bezeichung.setGeometry(QtCore.QRect(20, 50, 151, 20))
        self.lineEdit_Bezeichung.setObjectName("lineEdit_Bezeichung")
        self.lineEdit_offset_Y = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_Y.setGeometry(QtCore.QRect(130, 130, 121, 20))
        self.lineEdit_offset_Y.setText("")
        self.lineEdit_offset_Y.setObjectName("lineEdit_offset_Y")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_Rotation = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Rotation.setGeometry(QtCore.QRect(130, 160, 121, 20))
        self.lineEdit_Rotation.setText("")
        self.lineEdit_Rotation.setObjectName("lineEdit_Rotation")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 91, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_offset_X = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_X.setGeometry(QtCore.QRect(130, 100, 121, 20))
        self.lineEdit_offset_X.setObjectName("lineEdit_offset_X")
        self.pushButton_filePicker = QtWidgets.QPushButton(Dialog)
        self.pushButton_filePicker.setGeometry(QtCore.QRect(350, 220, 81, 23))
        self.pushButton_filePicker.setObjectName("pushButton_filePicker")
        self.lineEdit_pfad = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pfad.setGeometry(QtCore.QRect(30, 220, 291, 20))
        self.lineEdit_pfad.setObjectName("lineEdit_pfad")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_Geometrie_anpassen = QtWidgets.QPushButton(Dialog)
        self.pushButton_Geometrie_anpassen.setGeometry(QtCore.QRect(30, 270, 131, 23))
        self.pushButton_Geometrie_anpassen.setObjectName("pushButton_Geometrie_anpassen")
        self.pushButton_exportieren = QtWidgets.QPushButton(Dialog)
        self.pushButton_exportieren.setGeometry(QtCore.QRect(20, 520, 101, 23))
        self.pushButton_exportieren.setObjectName("pushButton_exportieren")
        self.pushButton_Laden = QtWidgets.QPushButton(Dialog)
        self.pushButton_Laden.setGeometry(QtCore.QRect(20, 490, 101, 23))
        self.pushButton_Laden.setObjectName("pushButton_Laden")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Schablone"))
        self.label.setText(_translate("Dialog", "Bezeichung"))
        self.label_6.setText(_translate("Dialog", "Offset X [mm]"))
        self.label_7.setText(_translate("Dialog", "Rotation [°]"))
        self.label_5.setText(_translate("Dialog", "Offset Y [mm]"))
        self.pushButton_filePicker.setText(_translate("Dialog", "Datei wählen"))
        self.label_2.setText(_translate("Dialog", "Geometrie"))
        self.pushButton_Geometrie_anpassen.setText(_translate("Dialog", "Geometrie anpassen"))
        self.pushButton_exportieren.setText(_translate("Dialog", "exportieren"))
        self.pushButton_Laden.setText(_translate("Dialog", "importieren"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
