import model_Schablone
from typing import List
import model_Offset
import my_QTreeWidgetItem
import model_Prozess


class Setups:

    def __init__(self, name=None, offset=None, schablonen=None):
        # self.offset = model_Offset.Offset()
        # self.name = "Setups"
        # self.schablonen: List[model_Schablone.Schablone] = []
        # self.schablonen.append(model_Schablone.Schablone())

        if name is None:
            self.name = "Setups"
        else:
            self.name = name

        self.offset = model_Offset.Offset()
        if isinstance(offset, dict):
            self.offset.__init__(**offset)
        elif isinstance(offset, model_Offset.Offset) and offset is not None:
            self.offset = offset

        self.schablonen: List[model_Schablone.Schablone] = []
        if schablonen is None:
            self.schablonen.append(model_Schablone.Schablone())
        elif isinstance(schablonen[0], dict):
            self.schablonen = []
            for le in schablonen:
                print("le")
                print(le)
                ab = model_Schablone.Schablone(**le)
                self.schablonen.append(ab)
        elif isinstance(schablonen[0], model_Schablone.Schablone) and schablonen[0] is not None:
            self.schablonen = schablonen