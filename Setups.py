import Schablone
from typing import List
import Offset
import my_QTreeWidgetItem
import Prozess


class Setups:

    def __init__(self, tree_item: my_QTreeWidgetItem.my_QTreeWidgetItem):
        self.offset = Offset.Offset()
        self.Name = "Setups"
        self.Schablonen: List[Schablone.Schablone] = []
        self.Schablonen.append(Schablone.Schablone())
