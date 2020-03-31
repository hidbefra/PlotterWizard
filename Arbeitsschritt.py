import Offset
import Schnittparameter
import Prozess


class Arbeitsschritt:

    anzahl = 1

    def __init__(self, parent):
        self.offset = Offset.Offset()
        self.schnittparameter = Schnittparameter.Schnittparameter()
        self.parent: Prozess.Prozess = parent
        self.Name = "Arbeitsschritt" + Arbeitsschritt.anzahl.__str__()
        Arbeitsschritt.anzahl += 1
        self.enabled = 2

