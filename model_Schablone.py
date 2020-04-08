import model_Offset
import model_Prozess
from typing import List




class Schablone:

    anzahl = 1

    def __init__(self):
        self.offset = model_Offset.Offset()
        self.name = "Schablone " + Schablone.anzahl.__str__()
        Schablone.anzahl += 1
        self.Prozesse: List[model_Prozess.Prozess] = []
        self.Prozesse.append(model_Prozess.Prozess(self))
        self.enabled = 2



