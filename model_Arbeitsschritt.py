import model_Offset
import model_Schnittparameter
import model_Prozess


class Arbeitsschritt:

    anzahl = 0

    def __init__(self, json=None, parent=None):
        Arbeitsschritt.anzahl += 1
        if (json==None):
            self.offset = model_Offset.Offset()
            self.schnittparameter = model_Schnittparameter.Schnittparameter()
            self.parent: model_Prozess.Prozess = parent
            self.name = "Arbeitsschritt" + Arbeitsschritt.anzahl.__str__()
            self.enabled = 2
        else:
            self.__dict__ = json
            self.parent = None



