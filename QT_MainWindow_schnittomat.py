# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_MainWindow_schnittomat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 870)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Stop.setGeometry(QtCore.QRect(580, 770, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(430, 770, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.treeWidget_Produktion = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_Produktion.setGeometry(QtCore.QRect(20, 110, 256, 701))
        self.treeWidget_Produktion.setMouseTracking(False)
        self.treeWidget_Produktion.setTabletTracking(False)
        self.treeWidget_Produktion.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.treeWidget_Produktion.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeWidget_Produktion.setExpandsOnDoubleClick(False)
        self.treeWidget_Produktion.setObjectName("treeWidget_Produktion")
        self.pushButton_hoch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hoch.setGeometry(QtCore.QRect(290, 270, 81, 23))
        self.pushButton_hoch.setObjectName("pushButton_hoch")
        self.pushButton_runter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_runter.setGeometry(QtCore.QRect(290, 300, 81, 23))
        self.pushButton_runter.setObjectName("pushButton_runter")
        self.pushButton_Schablone_hinzufgen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Schablone_hinzufgen.setGeometry(QtCore.QRect(280, 130, 171, 23))
        self.pushButton_Schablone_hinzufgen.setObjectName("pushButton_Schablone_hinzufgen")
        self.pushButton_Arbeitschrit_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Arbeitschrit_Delete.setGeometry(QtCore.QRect(290, 330, 81, 23))
        self.pushButton_Arbeitschrit_Delete.setObjectName("pushButton_Arbeitschrit_Delete")
        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit.setGeometry(QtCore.QRect(290, 240, 81, 23))
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.textEdit_Statu_Meldung = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Statu_Meldung.setEnabled(False)
        self.textEdit_Statu_Meldung.setGeometry(QtCore.QRect(320, 680, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_Statu_Meldung.setFont(font)
        self.textEdit_Statu_Meldung.setObjectName("textEdit_Statu_Meldung")
        self.pushButton_Prozess_hinzufgen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Prozess_hinzufgen.setGeometry(QtCore.QRect(310, 160, 141, 23))
        self.pushButton_Prozess_hinzufgen.setObjectName("pushButton_Prozess_hinzufgen")
        self.pushButton_Arbeitsschritt_hinzufgen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Arbeitsschritt_hinzufgen.setGeometry(QtCore.QRect(340, 190, 111, 23))
        self.pushButton_Arbeitsschritt_hinzufgen.setObjectName("pushButton_Arbeitsschritt_hinzufgen")
        self.textEdit_config_Name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_config_Name.setEnabled(True)
        self.textEdit_config_Name.setGeometry(QtCore.QRect(50, 20, 681, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_config_Name.setFont(font)
        self.textEdit_config_Name.setObjectName("textEdit_config_Name")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(470, 360, 256, 192))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionserial_communication = QtWidgets.QAction(MainWindow)
        self.actionserial_communication.setObjectName("actionserial_communication")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.menutest.addAction(self.actionserial_communication)
        self.menuDatei.addAction(self.actionOpen)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SchnittOmat"))
        self.pushButton_Stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_Start.setText(_translate("MainWindow", "Start"))
        self.treeWidget_Produktion.headerItem().setText(0, _translate("MainWindow", "Setups"))
        self.pushButton_hoch.setText(_translate("MainWindow", "hoch"))
        self.pushButton_runter.setText(_translate("MainWindow", "runter "))
        self.pushButton_Schablone_hinzufgen.setText(_translate("MainWindow", "add Schablone"))
        self.pushButton_Arbeitschrit_Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_edit.setText(_translate("MainWindow", "edit"))
        self.textEdit_Statu_Meldung.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">eine Kerbe einlegen</span></p></body></html>"))
        self.pushButton_Prozess_hinzufgen.setText(_translate("MainWindow", "add Prozess"))
        self.pushButton_Arbeitsschritt_hinzufgen.setText(_translate("MainWindow", "add Arbeitsschritt"))
        self.textEdit_config_Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">CV 95 A2</span></p></body></html>"))
        self.menutest.setTitle(_translate("MainWindow", "Setup"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionserial_communication.setText(_translate("MainWindow", "serial communication"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
