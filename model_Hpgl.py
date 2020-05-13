import model_Offset
import re
from typing import List
import copy


class HpglCommand:

    # offset: model_Offset = None
    re_patern = "([A-Z]{2})([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?"
    datatyp_dict = {"LL": float, "ML": float, "LF": int, "VS": float, "VU": float, "AS": int,
                    "QU": int, "XX": int, "PB": int, "EG": int, "PB": int, "PU": int,
                    "AA": [int, int, float], "SZ": float, "PW": float}

    def __init__(self,command="",parameters=[],prefix=None,suffix=None,code=None):
        self.command = command
        self.parameters = parameters
        # self.prefix: HpglCommand = prefix
        # self.suffix:HpglCommand = suffix

        if code is not None:
            self.decode(code)

        self.parameters = list(filter(("").__ne__, self.parameters)) #lehre stellen löschen

        self.prefix: HpglCommand = None
        if isinstance(prefix, dict):
            self.prefix.__init__(**prefix)
        elif isinstance(prefix, HpglCommand) and prefix is not None:
            self.prefix = prefix

        self.suffix: HpglCommand = None
        if isinstance(suffix, dict):
            self.suffix.__init__(**suffix)
        elif isinstance(suffix, HpglCommand) and suffix is not None:
            self.suffix = suffix

    def get_command(self):
        if self.command == "XX":
            if self.parameters[0] == "13":
                return self.command + self.parameters[0] + "," + self.parameters[1]
            else:
                return self.command + self.parameters[0]
        elif self.command == "PB":
            return self.command + self.parameters[0]
        else:
            return self.command

    def get_parameters(self, typ=None):
        if self.command == "XX":
            ret = self.parameters[1:]
        elif self.command == "PB":
            ret = self.parameters[1:]
        else:
            ret = self.parameters
        this_typ = typ
        if this_typ is None:
            if self.command in HpglCommand.datatyp_dict:
                this_typ = HpglCommand.datatyp_dict[self.command]
            else:
                this_typ = str

        if this_typ is int:
            return [int(x) if x is not "" else x for x in ret]
        elif this_typ is str:
            return [str(x) if x is not "" else x for x in ret]
        elif this_typ is float:
            return [float(x) if x is not "" else x for x in ret]

    def set_parameter(self,data):
        str_data = [str(x) if x is not "" else x for x in data]
        if self.command == "XX":
            if self.parameters[0] == "13":
                str_data.insert(0, self.parameters[1])
                str_data.insert(0, self.parameters[0])
                self.parameters = str_data
            else:
                str_data.insert(0, self.parameters[0])
                self.parameters = str_data
        elif self.command == "PB":
            str_data.insert(0, self.parameters[0])
            self.parameters = str_data
        else:
            self.parameters = str_data


    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)

    def decode(self, string: str):
        m = re.findall(HpglCommand.re_patern, string) #regex
        if m is not None:
            res = m[0]
            self.command = res[0]
            li = [*res[1:]] #list umpacken sonst giebt es ein tupel-> schreibgeschützt
            # if li[0] is "": #das muss sein weil sonst bei __init__ gewisse stellen lehr bleiben
            #     li[0] = "0"
            # elif li[1] is "":
            #     li[1] = "0"
            # elif li[2] is "":
            #     li[2] = "0"
            self.parameters = li

    def encode(self):
        return self.command + ",".join(self.parameters) + ";"

    # def set_offset(self,offset: model_Offset):
    #     HpglCommand.offset = offset


class Hpgl_structure:

    re_patern= "([A-Z]{2})([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?"

    def __init__(self, code="", offset=None, commands=None):

        self.code = code

        self.offset = model_Offset.Offset()
        if isinstance(offset, dict):
            self.offset.__init__(**offset)
        elif isinstance(offset, model_Offset.Offset) and offset is not None:
            self.offset = offset

        self.commands: List[HpglCommand] = []
        if commands is None:
            self.commands.append(HpglCommand())
        elif isinstance(commands[0], dict):
            self.commands = []
            for le in commands:
                ab = HpglCommand(**le)
                self.commands.append(ab)
        elif isinstance(commands[0], HpglCommand) and commands[0] is not None:
            self.commands = commands

    def decode(self):
        m = re.findall(Hpgl_structure.re_patern, self.code) #regex
        self.commands = []
        for res in m:
            self.commands.append(HpglCommand(command=res[0],parameters=res[1:]))

    def encode(self):
        command: HpglCommand
        data = ""
        for command in self.commands:
            data += command.encode() + "\n"
        return data

    def get_first_of(self,search_for_command: HpglCommand):
        ret = search_for_command
        coammand: HpglCommand
        for coammand in self.commands:
            if coammand.get_command() == search_for_command.get_command():
                ret = coammand
                break
        return ret

    def replace_all_command_with(self, data: HpglCommand):
        coammand: HpglCommand
        for coammand in self.commands:
            if coammand.get_command() == data.get_command():
                coammand.copy_from(data)


if __name__ == "__main__":
    test = HpglCommand(code="XX13,1")
    print(test.__dict__)