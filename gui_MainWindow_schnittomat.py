from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import gui_Arbeitsschritt
import gui_Schablone
import gui_Prozess
import Setups

import my_QTreeWidgetItem

import Schablone
import Prozess
import Arbeitsschritt

import QT_MainWindow_schnittomat as mw


class gui_MainWindow_schnittomat:

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.pushButton_Arbeitsschritt_hinzufgen.clicked.connect(self.pushButton_Arbeitsschritt_hinzufgen)
        self.ui.pushButton_Schablone_hinzufgen.clicked.connect(self.pushButton_Schablone_hinzufgen)
        self.ui.pushButton_Prozess_hinzufgen.clicked.connect(self.pushButton_Prozess_hinzufgen)

        self.ui.treeWidget_Produktion.itemDoubleClicked.connect(self.ondoubleclick)

        self.guiArbeitsschritt = gui_Arbeitsschritt.gui_Arbeitsschrit()
        self.guiSchablone = gui_Schablone.gui_Schablone()
        self.guiProzess = gui_Prozess.gui_Prozess()

        item = my_QTreeWidgetItem.my_QTreeWidgetItem(self.ui.treeWidget_Produktion)

        self.Setups = Setups.Setups(item) # erstellen des Models


    def show(self):
        self.MainWindow.show()


    def pushButton_Arbeitsschritt_hinzufgen(self):
        self.guiArbeitsschritt.show()


    def pushButton_Schablone_hinzufgen(self):

        item = my_QTreeWidgetItem.my_QTreeWidgetItem(self.ui.treeWidget_Produktion)
        item.setText(0, "Schablone")
        item.modul = Schablone.Schablone()
        self.ui.treeWidget_Produktion.addTopLevelItem(item)

        item2 = my_QTreeWidgetItem.my_QTreeWidgetItem(item)
        item2.setText(0, "Prozess")
        item2.modul = Prozess.Prozess()
        item.addChild(item2)

        item3 = my_QTreeWidgetItem.my_QTreeWidgetItem(item)
        item3.setText(0, "Arbeitsschritt")
        item3.modul = Arbeitsschritt.Arbeitsschritt()
        item2.addChild(item3)


    def pushButton_Prozess_hinzufgen(self):

        item = my_QTreeWidgetItem.my_QTreeWidgetItem(self.ui.treeWidget_Produktion)
        item.setText(0, "prozess")
        item.modul = Prozess.Prozess()
        self.ui.treeWidget_Produktion.addTopLevelItem(item)


    def ondoubleclick(self, previous):
        self.EditContent(self.ui.treeWidget_Produktion.currentItem().modul)


    def EditContent(self, modul: Prozess.Prozess):
        if type(modul) is Schablone.Schablone:
            print("EditContent für SChablone")
            self.guiSchablone.show(modul)

        if type(modul) is Prozess.Prozess:
            print("EditContent für Prozess")
            self.guiProzess.show(modul)

        if type(modul) is Arbeitsschritt.Arbeitsschritt:
            print("EditContent für Arbeitsschritt")
            self.guiArbeitsschritt.show(modul)
