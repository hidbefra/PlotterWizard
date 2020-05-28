from PyQt5 import QtCore, QtGui, QtWidgets
import my_Json
import os
import sys


class FileHandling:

    system_path = ""
    last_path = None
    path_of_open_projekt = None

    def __init__(self, extension):
        self.extension = extension

    def file_picker_save(self, pfad=None):
        if pfad is "":
            pfad = self.get_last_dir()
        fileName_struct = QtWidgets.QFileDialog.getSaveFileName(None,
                                                                "Save config to file",
                                                                pfad,
                                                                f"Config (*{self.extension})")
        return fileName_struct[0]

    def safe_projekt(self, data, name):
        if FileHandling.path_of_open_projekt is None:
            self.safe_projekt_as(data, name)
        else:
            self.save_json_file(data, FileHandling.path_of_open_projekt)
            print(f"Save Projekt: {name} unter {FileHandling.path_of_open_projekt}")

    def safe_projekt_as(self, data, name):
        path = self.file_picker_save(f"{self.get_last_dir()}\\{name}")
        if path:
            self.save_json_file(data, path)
            FileHandling.path_of_open_projekt = path
            print(f"Save Projekt: { name } unter {path}")

    def export_file(self, data, name):
        path = self.file_picker_save(f"{self.get_last_dir()}\\{name}")
        if path:
            self.save_json_file(data, path)
            self.safe_last_dir(path)
            print(f"export: {path}")

    def save_json_file(self, data, path):
        if path:
            self.safe(path, my_Json.dumps(data))

    def safe(self, path , data):
        try:
            f = open(path, "w+")
            f.write(data)
            f.close()
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def file_picker_open(self,pfad=None):
        if pfad is None:
            pfad = self.get_last_dir()
        fileName_struct = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                "Open config to file",
                                                                pfad,
                                                                f"Config (*{self.extension})")
        return fileName_struct[0]

    def open_projekt(self, pfad=None):
        data = None
        path = self.file_picker_open(pfad)
        if path:
            data = self.open_json_file(path)
            FileHandling.path_of_open_projekt = path
            print(f"projekt: {path} geöffnet")
        return data

    def import_file(self):
        data = None
        path = self.file_picker_open()
        if path:
            data = self.open_json_file(path)
            self.safe_last_dir(path)
            print(f"import: {path}")
        return data

    def open_json_file(self, pfad):
        data = None
        if pfad:
            data = my_Json.loads(self.open(pfad))
        return data

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

    def open_with_file_dialog(self):

        fileName_struct = QtWidgets.QFileDialog.getOpenFileName(None,
                                                                "Open config to file",
                                                                f"{self.get_last_dir()}")
        fileName = fileName_struct[0]
        if fileName:
            return self.open(fileName)

    def safe_last_dir(self,path):
        FileHandling.last_path = os.path.dirname(path)

    def get_last_dir(self):
        mydir = FileHandling.last_path
        if mydir is None:
            mydir = self.system_path
        return mydir