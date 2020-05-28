from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import _ui_translate
import gui_MainWindow_PlotterWizard
import os
import file_handling

def main():

    app = QtWidgets.QApplication(sys.argv)

    MainWindow_schnittomat = gui_MainWindow_PlotterWizard.gui_MainWindow_PlotterWizard()
    MainWindow_schnittomat.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()