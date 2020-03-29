import Schablone
from typing import List
import Offset
import my_QTreeWidgetItem


class Setups:

    Schablonen: List[Schablone.Schablone] = []

    def __init__(self,tree_item: my_QTreeWidgetItem):
        self.offset = Offset.Offset()
        self.name = "Setups"
        self.Schablonen.append(Schablone.Schablone())
        self.tree_item = tree_item
