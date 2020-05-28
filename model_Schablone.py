import model_Offset
import model_Prozess
from typing import List




class Schablone:

    anzahl = 0

    def __init__(self, name=None, enabled=None, offset=None, prozesse=None):
        # self.offset = model_Offset.Offset()
        # self.name = "Schablone " + Schablone.anzahl.__str__()
        # Schablone.anzahl += 1
        # self.Prozesse: List[model_Prozess.Prozess] = []
        # self.Prozesse.append(model_Prozess.Prozess())
        # self.enabled = 2


        Schablone.anzahl += 1

        if name is None:
            self.name = "Schablone" + Schablone.anzahl.__str__()
        else:
            self.name = name

        if enabled is None:
            self.enabled = 2
        else:
            self.enabled = enabled


        self.offset = model_Offset.Offset()
        if isinstance(offset, dict):
            self.offset.__init__(**offset)
        elif isinstance(offset, model_Offset.Offset) and offset is not None:
            self.offset = offset

        self.prozesse: List[model_Prozess.Prozess] = []
        if prozesse is None:
            self.prozesse.append(model_Prozess.Prozess())
        elif isinstance(prozesse[0], dict):
            self.prozesse = []
            for le in prozesse:
                ab = model_Prozess.Prozess(**le)
                self.prozesse.append(ab)
        elif isinstance(prozesse[0], model_Prozess.Prozess) and prozesse[0] is not None:
            self.prozesse = prozesse

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)