from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import _ui_translate
import gui_MainWindow_PlotterWizard
import os
import file_handling

def main():

    file_handling.FileHandling.system_path = os.path.dirname(os.path.realpath(__file__))

    app = QtWidgets.QApplication(sys.argv)

    MainWindow_schnittomat = gui_MainWindow_PlotterWizard.gui_MainWindow_schnittomat()
    MainWindow_schnittomat.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()