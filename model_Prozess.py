import model_Offset
import model_Arbeitsschritt
import model_Schablone
from typing import List


class Prozess:

    anzahl = 0

    def __init__(self, name=None, enabled=None, offset=None, arbeitsschritte=None):

        Prozess.anzahl += 1

        if name is None:
            self.name = "Prozess" + Prozess.anzahl.__str__()
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

        self.arbeitsschritte: List[model_Arbeitsschritt.Arbeitsschritt] = []
        if arbeitsschritte is None:
            self.arbeitsschritte.append(model_Arbeitsschritt.Arbeitsschritt())
        elif isinstance(arbeitsschritte[0], dict):
            self.arbeitsschritte = []
            for le in arbeitsschritte:
                ab = model_Arbeitsschritt.Arbeitsschritt(**le)
                self.arbeitsschritte.append(ab)
        elif isinstance(arbeitsschritte[0], model_Arbeitsschritt.Arbeitsschritt) and arbeitsschritte[0] is not None:
            self.arbeitsschritte = arbeitsschritte

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)