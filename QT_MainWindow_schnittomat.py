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
        MainWindow.resize(601, 870)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Stop.setGeometry(QtCore.QRect(300, 750, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(170, 750, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.treeWidget_Produktion = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_Produktion.setGeometry(QtCore.QRect(20, 110, 551, 541))
        self.treeWidget_Produktion.setMouseTracking(False)
        self.treeWidget_Produktion.setTabletTracking(False)
        self.treeWidget_Produktion.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.treeWidget_Produktion.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeWidget_Produktion.setExpandsOnDoubleClick(False)
        self.treeWidget_Produktion.setObjectName("treeWidget_Produktion")
        self.textEdit_Statu_Meldung = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Statu_Meldung.setEnabled(False)
        self.textEdit_Statu_Meldung.setGeometry(QtCore.QRect(20, 670, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_Statu_Meldung.setFont(font)
        self.textEdit_Statu_Meldung.setObjectName("textEdit_Statu_Meldung")
        self.textEdit_config_Name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_config_Name.setEnabled(True)
        self.textEdit_config_Name.setGeometry(QtCore.QRect(20, 30, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_config_Name.setFont(font)
        self.textEdit_config_Name.setObjectName("textEdit_config_Name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
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
        self.textEdit_Statu_Meldung.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">eine Kerbe einlegen</span></p></body></html>"))
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
