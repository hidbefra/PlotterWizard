

class Offset:

    def __init__(self, x=0, y=0, phi=0):
        self.x = x
        self.y = y
        self.phi = phi

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)
