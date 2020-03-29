from PyQt5 import QtCore, QtGui, QtWidgets


class my_QTreeWidgetItem(QtWidgets.QTreeWidgetItem):

    def __init__(self, parents):
        super().__init__()
        self.modul = None

