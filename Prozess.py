import Offset
import Arbeitsschritt
import Schablone
from typing import List


class Prozess:

    anzhal = 1

    def __init__(self, parent):
        self.offset = Offset.Offset()
        self.parent: Schablone.Schablone = parent
        self.Name = "Prozess" + Prozess.anzhal.__str__()
        Prozess.anzhal += 1
        self.Arbeitsschritte: List[Arbeitsschritt.Arbeitsschritt] = []
        self.Arbeitsschritte.append(Arbeitsschritt.Arbeitsschritt(self))
        self.enabled = 2