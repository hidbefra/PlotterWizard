# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Setups.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 231)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 180, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_offset_Y = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_Y.setGeometry(QtCore.QRect(130, 100, 121, 20))
        self.lineEdit_offset_Y.setText("")
        self.lineEdit_offset_Y.setObjectName("lineEdit_offset_Y")
        self.lineEdit_bezeichung = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_bezeichung.setGeometry(QtCore.QRect(20, 30, 291, 20))
        self.lineEdit_bezeichung.setObjectName("lineEdit_bezeichung")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Rotation = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Rotation.setGeometry(QtCore.QRect(130, 130, 121, 20))
        self.lineEdit_Rotation.setText("")
        self.lineEdit_Rotation.setObjectName("lineEdit_Rotation")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_offset_X = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_X.setGeometry(QtCore.QRect(130, 70, 121, 20))
        self.lineEdit_offset_X.setObjectName("lineEdit_offset_X")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setups"))
        self.label_2.setText(_translate("Dialog", "Bezeichnung"))
        self.label_3.setText(_translate("Dialog", "Offset X [mm]"))
        self.label_6.setText(_translate("Dialog", "Rotation [°]"))
        self.label_4.setText(_translate("Dialog", "Offset Y [mm]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
