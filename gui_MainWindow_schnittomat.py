from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import gui_Arbeitsschritt
import gui_Schablone
import gui_Prozess
import gui_Setups


import my_QTreeWidgetItem

import Setups
import Schablone
import Prozess
import Arbeitsschritt

import QT_MainWindow_schnittomat as mw


class gui_MainWindow_schnittomat:

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.treeWidget_Produktion.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeWidget_Produktion.customContextMenuRequested.connect(self.openMenu_treeItem)

        self.ui.pushButton_Arbeitsschritt_hinzufgen.clicked.connect(self.pushButton_Arbeitsschritt_hinzufgen)
        self.ui.pushButton_Schablone_hinzufgen.clicked.connect(self.pushButton_Schablone_hinzufgen)
        self.ui.pushButton_Prozess_hinzufgen.clicked.connect(self.pushButton_Prozess_hinzufgen)

        self.ui.treeWidget_Produktion.itemDoubleClicked.connect(self.ondoubleclick)
        self.ui.treeWidget_Produktion.itemChanged.connect(self.treeWidget_Produktion_itemChanged)
        self.ui.treeWidget_Produktion.itemClicked.connect(self.treeWidget_Produktion_clicked)

        self.treeWidget_Produktion_head: QtWidgets.QHeaderView = self.ui.treeWidget_Produktion.header()
        self.treeWidget_Produktion_head.setSectionsClickable(True)
        self.treeWidget_Produktion_head.sectionDoubleClicked.connect(self.treeWidget_Produktion_head_DoubleClicked)
        self.treeWidget_Produktion_head.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_Produktion_head.customContextMenuRequested.connect(self.openMenu_treeHead)

        # self.ui.treeWidget_Produktion.setAcceptDrops(True)
        # self.ui.treeWidget_Produktion.setDragEnabled(True)
        # self.ui.treeWidget_Produktion.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)



        self.guiArbeitsschritt = gui_Arbeitsschritt.gui_Arbeitsschrit()
        self.guiSchablone = gui_Schablone.gui_Schablone()
        self.guiProzess = gui_Prozess.gui_Prozess()
        self.guiSetups = gui_Setups.gui_Setups()

        # item = my_QTreeWidgetItem.my_QTreeWidgetItem(self.ui.treeWidget_Produktion)

        self.Setups = Setups.Setups(self.ui.treeWidget_Produktion) # erstellen des Models
        self.update_TreeWidget()

    def update_TreeWidget(self):

        self.ui.treeWidget_Produktion.clear()

        self.ui.treeWidget_Produktion.headerItem().setText(0, self.Setups.Name)

        for schablone in self.Setups.Schablonen:
            item = my_QTreeWidgetItem.my_QTreeWidgetItem(self.ui.treeWidget_Produktion)
            item.setText(0, schablone.Name)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(0, schablone.enabled)
            item.modul = schablone
            self.ui.treeWidget_Produktion.addTopLevelItem(item)

            for prozzess in schablone.Prozesse:
                item2 = my_QTreeWidgetItem.my_QTreeWidgetItem(item)
                item2.setText(0, prozzess.Name)
                item2.setFlags(item2.flags() | QtCore.Qt.ItemIsTristate| QtCore.Qt.ItemIsUserCheckable)
                item2.setCheckState(0, prozzess.enabled)
                item2.modul = prozzess
                item.addChild(item2)

                for arbeitsscritt in prozzess.Arbeitsschritte:
                    item3 = my_QTreeWidgetItem.my_QTreeWidgetItem(item)
                    item3.setText(0, arbeitsscritt.Name)
                    item3.setFlags(item3.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item3.setCheckState(0, arbeitsscritt.enabled)
                    item3.modul = arbeitsscritt
                    item2.addChild(item3)

        self.ui.treeWidget_Produktion.expandAll()

    def show(self):
        self.MainWindow.show()

    def pushButton_Arbeitsschritt_hinzufgen(self):
        pass

    def pushButton_Schablone_hinzufgen(self):
        pass

    def pushButton_Prozess_hinzufgen(self):
        pass

    def ondoubleclick(self, previous):
        self.edit_modul(self.ui.treeWidget_Produktion.currentItem().modul)

    def treeWidget_Produktion_clicked(self, event):
        self.ui.treeWidget_Produktion.clearSelection()
        print("item_clicked")
        print(event)

    def treeWidget_Produktion_itemChanged(self, event: my_QTreeWidgetItem.my_QTreeWidgetItem):
        print("item_Changed")
        print(event.checkState(0))
        event.modul.enabled = event.checkState(0)

    def treeWidget_Produktion_head_DoubleClicked(self, evebt):
        self.edit_modul(None)

    def edit_modul(self, modul):
        if type(modul) is Schablone.Schablone:
            print("EditContent für SChablone")
            self.guiSchablone.show(modul)

        if type(modul) is Prozess.Prozess:
            print("EditContent für Prozess")
            self.guiProzess.show(modul)

        if type(modul) is Arbeitsschritt.Arbeitsschritt:
            print("EditContent für Arbeitsschritt")
            self.guiArbeitsschritt.show(modul)

        if modul is None:
            print("EditContent für Setup")
            self.guiSetups.show(self.Setups)

        self.update_TreeWidget()

    def add_modul(self, modul):
        print(modul)
        if type(modul) is Schablone.Schablone:
            md: Schablone.Schablone = modul
            md.Prozesse.append(Prozess.Prozess(md))
            print("EditContent für SChablone")

        if type(modul) is Prozess.Prozess:
            print("EditContent für Prozess")
            md: Prozess.Prozess = modul
            md.Arbeitsschritte.append(Arbeitsschritt.Arbeitsschritt(md))

        if modul is None:
            print("EditContent für Setup")
            self.Setups.Schablonen.append(Schablone.Schablone())

        self.update_TreeWidget()

    def delete_modul(self, modul):
        if type(modul) is Schablone.Schablone:
            md: Schablone.Schablone = modul
            print("delete " + md.Name)
            self.Setups.Schablonen.remove(md)

        if type(modul) is Prozess.Prozess:
            md: Prozess.Prozess = modul
            print("delete " + md.Name)
            md.parent.Prozesse.remove(md)

        if type(modul) is Arbeitsschritt.Arbeitsschritt:
            md: Arbeitsschritt.Arbeitsschritt = modul
            print("delete " + md.Name)
            md.parent.Arbeitsschritte.remove(md)

        self.update_TreeWidget()

    def openMenu_treeItem(self, event: QtCore.QPoint):
        menu = QtWidgets.QMenu()
        edit = menu.addAction("edit")
        add = menu.addAction("add")
        delete = menu.addAction("delete")
        action = menu.exec_(self.ui.treeWidget_Produktion.mapToGlobal(event))

        if action == edit:
            if self.ui.treeWidget_Produktion.currentItem() is None:
                pass
            else:
                self.edit_modul(self.ui.treeWidget_Produktion.currentItem().modul)

        if action == add:
            if self.ui.treeWidget_Produktion.currentItem() is None:
                self.add_modul(None)
            else:
                self.add_modul(self.ui.treeWidget_Produktion.currentItem().modul)

        if action == delete:
            if self.ui.treeWidget_Produktion.currentItem() is None:
                pass
            else:
                self.delete_modul(self.ui.treeWidget_Produktion.currentItem().modul)

    def openMenu_treeHead(self, event: QtCore.QPoint):
        menu = QtWidgets.QMenu()
        add = menu.addAction("add")
        edit = menu.addAction("edit")
        action = menu.exec_(self.ui.treeWidget_Produktion.mapToGlobal(event))

        if action == add:
            self.add_modul(None)

        if action == edit:
            self.edit_modul(None)