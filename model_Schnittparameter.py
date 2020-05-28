from model_Hpgl import *
from typing import List


class Schnittparameter():
    anzahl = 0

    def __init__(self, name=None, parameter_dict=None, custom_schnittparameter=None):
        Schnittparameter.anzahl += 1

        if name is None:
            self.name = "Schnittparameter" + Schnittparameter.anzahl.__str__()
        else:
            self.name = name

        if custom_schnittparameter is None:
            self.custom_schnittparameter = False
        else:
            self.custom_schnittparameter = custom_schnittparameter

        # self.parameter: List[HpglCommand] = []
        # if parameter is None:
        #     self.parameter.append(HpglCommand())
        # elif isinstance(parameter[0], dict):
        #     self.parameter = []
        #     for le in parameter:
        #         print("le")
        #         print(le)
        #         ab = HpglCommand(**le)
        #         self.parameter.append(ab)
        # elif isinstance(parameter[0], HpglCommand) and parameter[0] is not None:
        #     self.parameter = parameter

        self.parameter_dict = {}
        if parameter_dict is None:
            self.add_named_parameter("LL0")
            self.add_named_parameter("ML0")
            self.add_named_parameter("LF0")
            self.add_named_parameter("VS0")
            self.add_named_parameter("VU0")
            self.add_named_parameter("AS0,0")
            self.add_named_parameter("QU0")
            self.add_named_parameter("XX13,3,0")
            self.add_named_parameter("PB2,0")
            self.add_named_parameter("PB4,0")
            self.add_named_parameter("EG,0")

        elif isinstance(parameter_dict, dict):
            self.parameter_dict = {}
            for le in parameter_dict:
                ab = HpglCommand(**parameter_dict[le])
                self.parameter_dict.update({ab.get_command(): ab})

    def add_named_parameter(self, value):
        mod = HpglCommand(code=value)
        self.parameter_dict.update({mod.get_command(): mod})

    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)
