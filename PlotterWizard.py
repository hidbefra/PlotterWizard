from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import _ui_translate
import gui_MainWindow_PlotterWizard
import os
import file_handling
import status_text



def main():

    app = QtWidgets.QApplication(sys.argv)

    MainWindow_PlotterWizard = gui_MainWindow_PlotterWizard.gui_MainWindow_PlotterWizard()
    status_text.status_text(MainWindow_PlotterWizard.update_status_Text)
    MainWindow_PlotterWizard.conact_Plotter()
    MainWindow_PlotterWizard.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()