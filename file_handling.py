from PyQt5 import QtCore, QtGui, QtWidgets
import my_Json
import os


class FileHandling:

    system_path = ""
    last_path = None

    def __init__(self, extension):
        self.extension = extension

    def safe_json_file(self, data, name):
        fileName_struct = QtWidgets.QFileDialog.getSaveFileName(None,
                                                                "Save config to file",
                                                                f"{self.get_last_dir()}\\{name}",
                                                                f"Config (*{self.extension})")
        fileName = fileName_struct[0]
        if fileName:
            f = open(fileName, "w+")
            f.write(my_Json.dumps(data))
            f.close()
            self.safe_last_dir(fileName)
            print(self.last_path)

    def open_json_file(self):
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

    def open_file(self):
        fileName_struct = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                "Open config to file",
                                                                f"{self.get_last_dir()}")
        fileName = fileName_struct[0]
        data = None
        if fileName:
            f = open(fileName, "r")
            data = f.read()
            f.close()
        return data

    def safe_last_dir(self,fileName):
        FileHandling.last_path = os.path.dirname(fileName)

    def get_last_dir(self):
        mydir = FileHandling.last_path
        if mydir is None:
            mydir = self.system_path
        return mydir