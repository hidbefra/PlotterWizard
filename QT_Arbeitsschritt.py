# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Arbeitsschritt.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
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
        self.pushButton_Geometrie_Importieren = QtWidgets.QPushButton(Dialog)
        self.pushButton_Geometrie_Importieren.setGeometry(QtCore.QRect(30, 390, 81, 23))
        self.pushButton_Geometrie_Importieren.setObjectName("pushButton_Geometrie_Importieren")
        self.lineEdit_bezeichung = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_bezeichung.setGeometry(QtCore.QRect(30, 50, 291, 20))
        self.lineEdit_bezeichung.setObjectName("lineEdit_bezeichung")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_Geometrie_anpassen = QtWidgets.QPushButton(Dialog)
        self.pushButton_Geometrie_anpassen.setGeometry(QtCore.QRect(300, 390, 131, 23))
        self.pushButton_Geometrie_anpassen.setObjectName("pushButton_Geometrie_anpassen")
        self.textBrowser_Geometrie = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_Geometrie.setGeometry(QtCore.QRect(30, 100, 401, 281))
        self.textBrowser_Geometrie.setReadOnly(False)
        self.textBrowser_Geometrie.setObjectName("textBrowser_Geometrie")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_Laden = QtWidgets.QPushButton(Dialog)
        self.pushButton_Laden.setGeometry(QtCore.QRect(10, 570, 101, 23))
        self.pushButton_Laden.setObjectName("pushButton_Laden")
        self.pushButton_exportieren = QtWidgets.QPushButton(Dialog)
        self.pushButton_exportieren.setGeometry(QtCore.QRect(10, 600, 101, 23))
        self.pushButton_exportieren.setObjectName("pushButton_exportieren")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 500, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_offset_X = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_X.setGeometry(QtCore.QRect(130, 470, 121, 20))
        self.lineEdit_offset_X.setObjectName("lineEdit_offset_X")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 470, 91, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Rotation = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Rotation.setGeometry(QtCore.QRect(130, 530, 121, 20))
        self.lineEdit_Rotation.setText("")
        self.lineEdit_Rotation.setObjectName("lineEdit_Rotation")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 530, 91, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_offset_Y = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_offset_Y.setGeometry(QtCore.QRect(130, 500, 121, 20))
        self.lineEdit_offset_Y.setText("")
        self.lineEdit_offset_Y.setObjectName("lineEdit_offset_Y")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 430, 254, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Schnittparameter = QtWidgets.QPushButton(self.widget)
        self.pushButton_Schnittparameter.setObjectName("pushButton_Schnittparameter")
        self.horizontalLayout.addWidget(self.pushButton_Schnittparameter)
        self.checkBox_extract_parameter = QtWidgets.QCheckBox(self.widget)
        self.checkBox_extract_parameter.setChecked(True)
        self.checkBox_extract_parameter.setObjectName("checkBox_extract_parameter")
        self.horizontalLayout.addWidget(self.checkBox_extract_parameter)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Arbeitsschritte"))
        self.pushButton_Geometrie_Importieren.setText(_translate("Dialog", "Datei wählen"))
        self.label_2.setText(_translate("Dialog", "Bezeichnung"))
        self.pushButton_Geometrie_anpassen.setText(_translate("Dialog", "Geometrie anpassen"))
        self.label_5.setText(_translate("Dialog", "Geometrie"))
        self.pushButton_Laden.setText(_translate("Dialog", "importieren"))
        self.pushButton_exportieren.setText(_translate("Dialog", "exportieren"))
        self.label_4.setText(_translate("Dialog", "Offset Y [mm]"))
        self.label_3.setText(_translate("Dialog", "Offset X [mm]"))
        self.label_6.setText(_translate("Dialog", "Rotation [°]"))
        self.pushButton_Schnittparameter.setText(_translate("Dialog", "Schnittparameter"))
        self.checkBox_extract_parameter.setText(_translate("Dialog", "aus Geometrie übernehmen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
