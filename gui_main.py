from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ui_translate
import gui_MainWindow_schnittomat


def main():
    app = QtWidgets.QApplication(sys.argv)

    MainWindow_schnittomat = gui_MainWindow_schnittomat.gui_MainWindow_schnittomat()
    MainWindow_schnittomat.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()