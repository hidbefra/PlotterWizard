

class Schnittparameter():
    anzahl = 0

    def __init__(self, name=None):
        Schnittparameter.anzahl += 1

        if name is None:
            self.name = "Schnittparameter" + Schnittparameter.anzahl.__str__()
        else:
            self.name = name


