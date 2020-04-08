import model_Schablone
from typing import List
import model_Offset
import my_QTreeWidgetItem
import model_Prozess


class Setups:

    def __init__(self, tree_item: my_QTreeWidgetItem.my_QTreeWidgetItem):
        self.offset = model_Offset.Offset()
        self.name = "Setups"
        self.Schablonen: List[model_Schablone.Schablone] = []
        self.Schablonen.append(model_Schablone.Schablone())
