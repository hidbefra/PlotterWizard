from PyQt5 import QtCore, QtGui, QtWidgets
import my_Json
import os
import sys


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
            # f = open(fileName, "w+")
            # f.write(my_Json.dumps(data))
            # f.close()
            self.safe(fileName, my_Json.dumps(data))
            self.safe_last_dir(fileName)
            print(self.last_path)

    def safe(self, fileName , data):
        try:
            f = open(fileName, "w+")
            f.write(data)
            f.close()
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def open_json_file(self):
        fileName_struct = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                "Open config to file",
                                                                f"{self.get_last_dir()}",
                                                                f"Config (*{self.extension})")
        fileName = fileName_struct[0]
        data = None
        if fileName:
            #     f = open(fileName, "r")
            #     data = my_Json.loads(f.read())
            #     f.close()
            #     self.safe_last_dir(fileName)
            data = my_Json.loads(self.open(fileName))
        return data

    def open_with_file_dialog(self):

        fileName_struct = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                "Open config to file",
                                                                f"{self.get_last_dir()}")
        fileName = fileName_struct[0]


        # data = None
        if fileName:
            #     f = open(fileName, "r")
            #     data = f.read()
            #     f.close()
            # return data
            return self.open(fileName)

    def open(self, path):
        try:
            data = None
            f = open(path, "r")
            data = f.read()
            f.close()
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])

        return data

    def safe_last_dir(self,fileName):
        FileHandling.last_path = os.path.dirname(fileName)

    def get_last_dir(self):
        mydir = FileHandling.last_path
        if mydir is None:
            mydir = self.system_path
        return mydir