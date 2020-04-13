from PyQt5 import QtCore, QtGui, QtWidgets
import my_Json
import os


class FileHandling:

    system_path = ""


    def __init__(self, extension):
        self.extension = extension
        self.last_path = None

    def safe_file(self,data,name):
        fileName_struct = QtWidgets.QFileDialog.getSaveFileName(None,
                                                                "Save config to file",
                                                                f"{self.get_last_dir()}//{name}",
                                                                f"Config (*{self.extension})")
        fileName = fileName_struct[0]
        if fileName:
            f = open(fileName, "w+")
            f.write(my_Json.dumps(data))
            f.close()
            self.safe_last_dir(fileName)
            print(self.last_path)

    def open_file(self):
        fileName_struct = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                "Open config to file",
                                                                f"{self.get_last_dir()}",
                                                                f"Config (*{self.extension})")
        fileName = fileName_struct[0]
        data = None
        if fileName:
            f = open(fileName, "r")
            data = my_Json.loads(f.read())
            f.close()
            self.safe_last_dir(fileName)
        return data

    def safe_last_dir(self,fileName):
        self.last_path = os.path.dirname(fileName)

    def get_last_dir(self):
        mydir = self.last_path
        if mydir is None:
            mydir = self.system_path
        return mydir