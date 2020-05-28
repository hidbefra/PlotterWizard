import model_Schablone
from typing import List
import model_Offset
import my_QTreeWidgetItem
import model_Prozess
import  model_Arbeitsschritt
import copy


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
                ab = model_Schablone.Schablone(**le)
                self.schablonen.append(ab)
        elif isinstance(schablonen[0], model_Schablone.Schablone) and schablonen[0] is not None:
            self.schablonen = schablonen

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)

    def reorder(self):
        prozess_list: List[model_Prozess.Prozess] = []
        # neu ordnen. von jeder Schablone den ersten Prozess dan von jeder Schablone den zweiten Prozess usw.
        schabloneposition = 0
        for schablone in self.schablonen:
            insertposition = schabloneposition
            schritt = schabloneposition + 1
            schablone_offset = schablone.offset
            for prozess in schablone.prozesse:
                prozess_offset = prozess.offset
                arbeitsschritt_list=[]
                for arbeitsschritt in prozess.arbeitsschritte:
                    next_arbeitsschritt: model_Arbeitsschritt.Arbeitsschritt = copy.deepcopy(arbeitsschritt)

                    next_arbeitsschritt.offset.add(self.offset) #Setup offset
                    next_arbeitsschritt.offset.add(schablone_offset)
                    next_arbeitsschritt.offset.add(prozess_offset)

                    arbeitsschritt_list.append(next_arbeitsschritt)

                prozess_list.insert(insertposition,arbeitsschritt_list)
                insertposition = insertposition + schritt
            schabloneposition +=1

        prozess_list[0][0].offset.add(model_Offset.Offset(1,2,3))
        return prozess_list

    def encode(self):

        hpgl_cod = ""
        prozess_list = self.reorder()

        for arbeitsschritt_list in prozess_list:
            for arbeitsschritt in arbeitsschritt_list:
                arbeitsschritt.assign_correction()
                hpgl_cod = hpgl_cod + arbeitsschritt.hpgl_structure.encode()
        return hpgl_cod



