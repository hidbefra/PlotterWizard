import Offset
import Arbeitsschritt
from typing import List

class Prozess:

    Arbeitsschritte: List[Arbeitsschritt.Arbeitsschritt] = []

    def __init__(self):
        self.offset = Offset.Offset()
        self.Name = "Prozess"
        self.Arbeitsschritte.append(Arbeitsschritt.Arbeitsschritt())