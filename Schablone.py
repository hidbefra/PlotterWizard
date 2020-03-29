import Offset
import Prozess
from typing import List
import gui_Schablone



class Schablone:

    Prozesse: List[Prozess.Prozess] = []

    def __init__(self):
        self.offset = Offset.Offset()
        self.Name = "Schablone"
        self.Prozesse.append(Prozess.Prozess())


