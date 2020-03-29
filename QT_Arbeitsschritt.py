# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Arbeitsschritt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 642)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 590, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_pfad = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pfad.setGeometry(QtCore.QRect(30, 170, 291, 20))
        self.lineEdit_pfad.setObjectName("lineEdit_pfad")
        self.pushButton_filePicker = QtWidgets.QPushButton(Dialog)
        self.pushButton_filePicker.setGeometry(QtCore.QRect(350, 170, 81, 23))
        self.pushButton_filePicker.setObjectName("pushButton_filePicker")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 150, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit_bezeichung = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_bezeichung.setGeometry(QtCore.QRect(30, 50, 291, 20))
        self.lineEdit_bezeichung.setObjectName("lineEdit_bezeichung")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_Schnittparameter = QtWidgets.QPushButton(Dialog)
        self.pushButton_Schnittparameter.setGeometry(QtCore.QRect(30, 100, 121, 23))
        self.pushButton_Schnittparameter.setObjectName("pushButton_Schnittparameter")
        self.pushButton_Geometrie_anpassen = QtWidgets.QPushButton(Dialog)
        self.pushButton_Geometrie_anpassen.setGeometry(QtCore.QRect(40, 480, 131, 23))
        self.pushButton_Geometrie_anpassen.setObjectName("pushButton_Geometrie_anpassen")
        self.textBrowser_Geometrie = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_Geometrie.setGeometry(QtCore.QRect(30, 230, 401, 141))
        self.textBrowser_Geometrie.setObjectName("textBrowser_Geometrie")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 47, 13))
        self.label_5.setObjectName("label_5")
        self.pushButton_Laden = QtWidgets.QPushButton(Dialog)
        self.pushButton_Laden.setGeometry(QtCore.QRect(10, 570, 101, 23))
        self.pushButton_Laden.setObjectName("pushButton_Laden")
        self.pushButton_exportieren = QtWidgets.QPushButton(Dialog)
        self.pushButton_exportieren.setGeometry(QtCore.QRect(10, 600, 101, 23))
        self.pushButton_exportieren.setObjectName("pushButton_exportieren")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 410, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_offset_X = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_X.setGeometry(QtCore.QRect(140, 380, 121, 20))
        self.lineEdit_offset_X.setObjectName("lineEdit_offset_X")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 380, 91, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Rotation = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Rotation.setGeometry(QtCore.QRect(140, 440, 121, 20))
        self.lineEdit_Rotation.setText("")
        self.lineEdit_Rotation.setObjectName("lineEdit_Rotation")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 440, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_offset_Y = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_Y.setGeometry(QtCore.QRect(140, 410, 121, 20))
        self.lineEdit_offset_Y.setText("")
        self.lineEdit_offset_Y.setObjectName("lineEdit_offset_Y")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Arbeitsschritte"))
        self.pushButton_filePicker.setText(_translate("Dialog", "Datei wählen"))
        self.label.setText(_translate("Dialog", "Geometrie"))
        self.label_2.setText(_translate("Dialog", "Bezeichnung"))
        self.pushButton_Schnittparameter.setText(_translate("Dialog", "Schnittparameter"))
        self.pushButton_Geometrie_anpassen.setText(_translate("Dialog", "Geometrie anpassen"))
        self.label_5.setText(_translate("Dialog", "Geometrie"))
        self.pushButton_Laden.setText(_translate("Dialog", "importieren"))
        self.pushButton_exportieren.setText(_translate("Dialog", "exportieren"))
        self.label_4.setText(_translate("Dialog", "Offset Y [mm]"))
        self.label_3.setText(_translate("Dialog", "Offset X [mm]"))
        self.label_6.setText(_translate("Dialog", "Rotation [°]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
