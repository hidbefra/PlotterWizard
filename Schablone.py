import Offset
import Prozess
from typing import List




class Schablone:

    anzahl = 1

    def __init__(self):
        self.offset = Offset.Offset()
        self.Name = "Schablone " + Schablone.anzahl.__str__()
        Schablone.anzahl += 1
        self.Prozesse: List[Prozess.Prozess] = []
        self.Prozesse.append(Prozess.Prozess(self))
        self.enabled = 2



