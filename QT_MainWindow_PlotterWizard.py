# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_MainWindow_PlotterWizard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 917)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Stop.setGeometry(QtCore.QRect(300, 790, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(170, 790, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Start.setFont(font)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.treeWidget_Produktion = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_Produktion.setGeometry(QtCore.QRect(20, 110, 551, 591))
        self.treeWidget_Produktion.setMaximumSize(QtCore.QSize(16777215, 591))
        self.treeWidget_Produktion.setMouseTracking(False)
        self.treeWidget_Produktion.setTabletTracking(False)
        self.treeWidget_Produktion.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.treeWidget_Produktion.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeWidget_Produktion.setExpandsOnDoubleClick(False)
        self.treeWidget_Produktion.setObjectName("treeWidget_Produktion")
        self.textEdit_Statu_Meldung = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Statu_Meldung.setEnabled(False)
        self.textEdit_Statu_Meldung.setGeometry(QtCore.QRect(20, 710, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_Statu_Meldung.setFont(font)
        self.textEdit_Statu_Meldung.setObjectName("textEdit_Statu_Meldung")
        self.textEdit_config_Name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_config_Name.setEnabled(True)
        self.textEdit_config_Name.setGeometry(QtCore.QRect(20, 30, 551, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_config_Name.sizePolicy().hasHeightForWidth())
        self.textEdit_config_Name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit_config_Name.setFont(font)
        self.textEdit_config_Name.setObjectName("textEdit_config_Name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/71.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew.setIcon(icon)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/1959.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsave.setIcon(icon1)
        self.actionsave.setObjectName("actionsave")
        self.actionopen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/1951.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon2)
        self.actionopen.setObjectName("actionopen")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/2413.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon3)
        self.actionSettings.setObjectName("actionSettings")
        self.menutest.addAction(self.actionSettings)
        self.menuDatei.addAction(self.actionopen)
        self.menuDatei.addAction(self.actionnew)
        self.menuDatei.addAction(self.actionsave)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menutest.menuAction())
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addAction(self.actionnew)

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
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menutest.setTitle(_translate("MainWindow", "Setup"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
import QT_Designer_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
