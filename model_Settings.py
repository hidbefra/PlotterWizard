

class Settings:

    def __init__(self, RS232_port=None):

        if RS232_port is None:
            self.RS232_port = ""
        else:
            self.RS232_port = RS232_port

        self.restore_default()
        pass

    def restore_default(self):
        self.RS232_port = "COM3"

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)