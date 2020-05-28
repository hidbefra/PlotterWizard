import model_Offset
import model_Schnittparameter
import model_Prozess
from model_Hpgl import *


class Arbeitsschritt:

    anzahl = 0

    def __init__(self, name=None, enabled=None, offset=None, schnittparameter=None, hpgl_structure=None):
        Arbeitsschritt.anzahl += 1

        if name is None:
            self.name = "Arbeitsschritt" + Arbeitsschritt.anzahl.__str__()
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

        self.schnittparameter = model_Schnittparameter.Schnittparameter()
        if isinstance(schnittparameter, dict):
            self.schnittparameter.__init__(**schnittparameter)
        elif isinstance(schnittparameter, model_Schnittparameter.Schnittparameter) and schnittparameter is not None:
            self.schnittparameter = schnittparameter

        self.hpgl_structure = Hpgl_structure()
        if isinstance(hpgl_structure, dict):
            self.hpgl_structure.__init__(**hpgl_structure)
        elif isinstance(hpgl_structure, Hpgl_structure) and hpgl_structure is not None:
            self.hpgl_structure = hpgl_structure

    def schnittparameter_decode(self): # suche nach den schnittparameter im HPGL cod
        for key in self.schnittparameter.parameter_dict:
            self.schnittparameter.parameter_dict[key] = self.hpgl_structure.get_first_of(self.schnittparameter.parameter_dict[key])
        pass

    def assigned_new_schnittparameter(self):
        for key in self.schnittparameter.parameter_dict:
            self.hpgl_structure.replace_all_command_with(self.schnittparameter.parameter_dict[key])

    def assign_correction(self):
        self.hpgl_structure.assign_correction(self.offset)

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)
