from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from itertools import cycle
import os

import gui_Arbeitsschritt
import gui_Schablone
import gui_Prozess
import gui_Setups
import gui_Sttings

import my_QTreeWidgetItem

import model_Setups
import model_Schablone
import model_Prozess
import model_Arbeitsschritt
import model_Settings
import model_Plotter

from file_handling import FileHandling

import QT_MainWindow_PlotterWizard as mw

from status_text import status_text



class gui_MainWindow_PlotterWizard():

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.treeWidget_Produktion.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeWidget_Produktion.customContextMenuRequested.connect(self.openMenu_treeItem)

        # self.ui.pushButton_Arbeitsschritt_hinzufgen.clicked.connect(self.pushButton_Arbeitsschritt_hinzufgen)
        # self.ui.pushButton_Schablone_hinzufgen.clicked.connect(self.pushButton_Schablone_hinzufgen)
        # self.ui.pushButton_Prozess_hinzufgen.clicked.connect(self.pushButton_Prozess_hinzufgen)
        self.ui.pushButton_Start.clicked.connect(self.pushButton_Start)
        self.ui.pushButton_Stop.clicked.connect(self.pushButton_Stop)

        self.ui.treeWidget_Produktion.itemDoubleClicked.connect(self.ondoubleclick)
        self.ui.treeWidget_Produktion.itemChanged.connect(self.treeWidget_Produktion_itemChanged)
        self.ui.treeWidget_Produktion.itemClicked.connect(self.treeWidget_Produktion_clicked)

        self.ui.actionopen.triggered.connect(self.actionOpen_clicked)
        self.ui.actionnew.triggered.connect(self.actionnew_clicked)
        self.ui.actionsave.triggered.connect(self.actionsave_clicked)
        self.ui.actionSettings.triggered.connect(self.actionSettings_clicked)
        self.ui.actionsave_as.triggered.connect(self.actionsave_as_clicked)

        self.treeWidget_Produktion_head: QtWidgets.QHeaderView = self.ui.treeWidget_Produktion.header()
        self.treeWidget_Produktion_head.setSectionsClickable(True)
        self.treeWidget_Produktion_head.sectionDoubleClicked.connect(self.treeWidget_Produktion_head_DoubleClicked)
        self.treeWidget_Produktion_head.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_Produktion_head.customContextMenuRequested.connect(self.openMenu_treeHead)


        # self.ui.treeWidget_Produktion.setAcceptDrops(True)
        # self.ui.treeWidget_Produktion.setDragEnabled(True)
        # self.ui.treeWidget_Produktion.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        self.guiArbeitsschritt = gui_Arbeitsschritt.gui_Arbeitsschrit(self.MainWindow)
        self.guiSchablone = gui_Schablone.gui_Schablone(self.MainWindow)
        self.guiProzess = gui_Prozess.gui_Prozess(self.MainWindow)
        self.guiSetups = gui_Setups.gui_Setups(self.MainWindow)

        # item = my_QTreeWidgetItem.my_QTreeWidgetItem(self.ui.treeWidget_Produktion)

        self.filehandeling = FileHandling(".set")

        self.setups = model_Setups.Setups()  # erstellen des Models
        self.running = False

        self.parents = {}  # um die elemente im treeWidget löschen zu können weird eine Referenz auf das Elter benötigt

        self.update_TreeWidget()

        FileHandling.system_path = os.path.dirname(sys.argv[0]) # os.path.dirname(os.path.realpath(__file__))
        self.settings = model_Settings.Settings()
        FileHandling.last_path = self.settings.setings["ablage"]["Pfad Programme"]

        self.plotter: model_Plotter.Plotter

        #self.status_text = ""
        self.update_gui()

    def conact_Plotter(self):
        self.plotter = model_Plotter.Plotter(self.settings)

    def update_gui(self):
        pass

    def update_status_Text(self):
        self.ui.textEdit_Statu_Meldung.setText(status_text.text)
        self.ui.textEdit_Statu_Meldung.moveCursor(QtGui.QTextCursor.End)


    def update_TreeWidget(self):

        self.ui.treeWidget_Produktion.clear()

        self.ui.treeWidget_Produktion.headerItem().setText(0, self.setups.name)
        self.parents = {}
        for schablone in self.setups.schablonen:
            item = my_QTreeWidgetItem.my_QTreeWidgetItem(self.ui.treeWidget_Produktion)
            item.setText(0, schablone.name)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(0, schablone.enabled)
            item.modul = schablone
            self.ui.treeWidget_Produktion.addTopLevelItem(item)
            self.parents[id(schablone)] = self.setups.schablonen

            for prozzess in schablone.prozesse:
                item2 = my_QTreeWidgetItem.my_QTreeWidgetItem(item)
                item2.setText(0, prozzess.name)
                item2.setFlags(item2.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
                item2.setCheckState(0, prozzess.enabled)
                item2.modul = prozzess
                item.addChild(item2)
                self.parents[id(prozzess)] = schablone.prozesse

                for arbeitsscritt in prozzess.arbeitsschritte:
                    item3 = my_QTreeWidgetItem.my_QTreeWidgetItem(item)
                    item3.setText(0, arbeitsscritt.name)
                    item3.setFlags(item3.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item3.setCheckState(0, arbeitsscritt.enabled)
                    item3.modul = arbeitsscritt
                    item2.addChild(item3)
                    self.parents[id(arbeitsscritt)] = prozzess.arbeitsschritte

        self.ui.treeWidget_Produktion.expandAll()

    def show(self):
        self.MainWindow.show()


    def pushButton_Start(self):
        self.running = True
        self.plotter.prozess_init(self.setups.encode())
        self.plotter.prozess_start()
        self.update_gui()

    def pushButton_Stop(self):
        self.running = False
        self.plotter.prozess_stop()
        self.update_gui()
        pass

    def ondoubleclick(self, previous):
        self.edit_modul(self.ui.treeWidget_Produktion.currentItem().modul)

    def treeWidget_Produktion_clicked(self, event):
        self.ui.treeWidget_Produktion.clearSelection()

    def treeWidget_Produktion_itemChanged(self, event: my_QTreeWidgetItem.my_QTreeWidgetItem):
        event.modul.enabled = event.checkState(0)

    def treeWidget_Produktion_head_DoubleClicked(self, evebt):
        self.edit_modul(None)

    def edit_modul(self, modul):
        if type(modul) is model_Schablone.Schablone:
            self.guiSchablone.show(modul)

        if type(modul) is model_Prozess.Prozess:
            self.guiProzess.show(modul)

        if type(modul) is model_Arbeitsschritt.Arbeitsschritt:
            self.guiArbeitsschritt.show(modul)

        if modul is None:
            self.guiSetups.show(self.setups)

        self.update_TreeWidget()

    def add_modul(self, modul):
        if type(modul) is model_Schablone.Schablone:
            md: model_Schablone.Schablone = modul
            md.prozesse.append(model_Prozess.Prozess())

        if type(modul) is model_Prozess.Prozess:
            md: model_Prozess.Prozess = modul
            md.arbeitsschritte.append(model_Arbeitsschritt.Arbeitsschritt())

        if modul is None:
            self.setups.schablonen.append(model_Schablone.Schablone())

        self.update_TreeWidget()

    def delete_modul(self, modul):
        if type(modul) is model_Schablone.Schablone:
            md: model_Schablone.Schablone = modul
            self.parents[id(md)].remove(md)

        if type(modul) is model_Prozess.Prozess:
            md: model_Prozess.Prozess = modul
            self.parents[id(md)].remove(md)

        if type(modul) is model_Arbeitsschritt.Arbeitsschritt:
            md: model_Arbeitsschritt.Arbeitsschritt = modul
            self.parents[id(md)].remove(md)

        self.update_TreeWidget()

    def move_up(self, modul):
        if type(modul) is model_Schablone.Schablone:
            md: model_Schablone.Schablone = modul
            liste = self.parents[id(md)]
            oldindex = liste.index(md)
            if oldindex > 0:
                liste.insert(oldindex-1, liste.pop(oldindex))

        if type(modul) is model_Prozess.Prozess:
            md: model_Prozess.Prozess = modul
            liste = self.parents[id(md)]
            oldindex = liste.index(md)
            if oldindex > 0:
                liste.insert(oldindex-1, liste.pop(oldindex))

        if type(modul) is model_Arbeitsschritt.Arbeitsschritt:
            md: model_Arbeitsschritt.Arbeitsschritt = modul
            liste = self.parents[id(md)]
            oldindex = liste.index(md)
            if oldindex > 0:
                liste.insert(oldindex-1, liste.pop(oldindex))

        self.update_TreeWidget()

    def move_down(self, modul):
        if type(modul) is model_Schablone.Schablone:
            md: model_Schablone.Schablone = modul
            liste = self.parents[id(md)]
            oldindex = liste.index(md)
            if oldindex < len(liste):
                liste.insert(oldindex+1, liste.pop(oldindex))

        if type(modul) is model_Prozess.Prozess:
            md: model_Prozess.Prozess = modul
            liste = self.parents[id(md)]
            oldindex = liste.index(md)
            if oldindex < len(liste):
                liste.insert(oldindex+1, liste.pop(oldindex))

        if type(modul) is model_Arbeitsschritt.Arbeitsschritt:
            md: model_Arbeitsschritt.Arbeitsschritt = modul
            liste = self.parents[id(md)]
            oldindex = liste.index(md)
            if oldindex < len(liste):
                liste.insert(oldindex+1, liste.pop(oldindex))

        self.update_TreeWidget()


    def openMenu_treeItem(self, event: QtCore.QPoint):
        menu = QtWidgets.QMenu()
        edit = menu.addAction("edit")
        add = menu.addAction("add")
        delete = menu.addAction("delete")
        move_up = menu.addAction("move up")
        move_down = menu.addAction("move down")
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

        if action == move_up:
            if self.ui.treeWidget_Produktion.currentItem() is None:
                pass
            else:
                self.move_up(self.ui.treeWidget_Produktion.currentItem().modul)

        if action == move_down:
            if self.ui.treeWidget_Produktion.currentItem() is None:
                pass
            else:
                self.move_down(self.ui.treeWidget_Produktion.currentItem().modul)

    def openMenu_treeHead(self, event: QtCore.QPoint):
        menu = QtWidgets.QMenu()
        add = menu.addAction("add")
        edit = menu.addAction("edit")
        action = menu.exec_(self.ui.treeWidget_Produktion.mapToGlobal(event))

        if action == add:
            self.add_modul(None)

        if action == edit:
            self.edit_modul(None)

    def actionOpen_clicked(self):
        data = self.filehandeling.open_projekt(self.settings.setings["ablage"]["Pfad Programme"])
        if data is not None:
            self.setups.__init__(**data)
        self.update_TreeWidget()
        self.update_gui()

    def actionnew_clicked(self):
        FileHandling.path_of_open_projekt = None
        self.setups = model_Setups.Setups()
        self.update_TreeWidget()

    def actionsave_clicked(self):
        self.filehandeling.safe_projekt(self.setups, self.setups.name)

    def actionsave_as_clicked(self):
        self.filehandeling.safe_projekt_as(self.setups, self.setups.name)

    def actionSettings_clicked(self):
        gui = gui_Sttings.gui_Settings(self.MainWindow, self.settings)
        gui.show()
        self.pushButton_Stop()
        self.plotter.reinit_rs232(self.settings)
        self.update_gui()

