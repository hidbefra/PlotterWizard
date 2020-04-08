

class Schnittparameter:
    anzahl = 0

    def __init__(self, json=None):
        Schnittparameter.anzahl += 1
        if (json == None):
            self.name = "Schnittparameter" + Schnittparameter.anzahl.__str__()
        else:
            self.__dict__ = json
