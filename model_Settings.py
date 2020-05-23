from file_handling import FileHandling
import my_Json
import os.path

class Settings(FileHandling):

    _settings_name = "PlotterWizard.settings"

    def __init__(self):

        FileHandling.__init__(self, ".settings")
        self.setings = {}
        self._setings_file = self.system_path + "\\"+self._settings_name

        if os.path.isfile(self._setings_file):
            self.load_settings()
        else:
            self.restore_default()
            self.safe_settings()
        pass

    def load_settings(self):
        set = self.open(self._setings_file)
        self.setings =my_Json.loads(set)
        pass

    def safe_settings(self):
        self.safe(self._setings_file,my_Json.dumps(self.setings))
        pass

    def restore_default(self):
        self.setings = {
            "RS232port": "COM3",
            "baudrate": 19200,
            "parity": "N",
            "stopbits": 1,
            "bytesize": 8,
            "timeout": 1,
            "xonxoff": 0,
            "rtscts": 1
        }

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)