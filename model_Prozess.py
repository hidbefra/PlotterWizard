import model_Offset
import model_Arbeitsschritt
import model_Schablone
from typing import List


class Prozess:

    anzhal = 1

    def __init__(self, parent):
        self.offset = model_Offset.Offset()
        self.parent: model_Schablone.Schablone = parent
        self.name = "Prozess" + Prozess.anzhal.__str__()
        Prozess.anzhal += 1
        self.Arbeitsschritte: List[model_Arbeitsschritt.Arbeitsschritt] = []
        self.Arbeitsschritte.append(model_Arbeitsschritt.Arbeitsschritt(None, self))
        self.enabled = 2