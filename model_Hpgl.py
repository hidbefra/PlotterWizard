import model_Offset
import re
from typing import List
import copy


class HpglCommand:

    # offset: model_Offset = None
    re_patern = "([A-Z]{2})([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?"
    # re_patern = "([A-Z]{2})(?:([-\d.]+)(?:,|;))+"
    datatyp_dict = {"LL": [float],
                    "ML": [float],
                    "LF": [int],
                    "VS": [float, float],
                    "VU": [float],
                    "AS": [int, int],
                    "QU": [int],
                    "XX": [int, int, int, int],
                    "PB": [int, int, int],
                    "EG": [int],
                    "PU": [int,int],
                    "PD": [int,int],
                    "PR": [int, int],
                    "AA": [int, int, float],
                    "SZ": [float,float],
                    "PW": [int, int, int, int, int, int]}

    def __init__(self, _command="", _parameters=[], prefix=None, suffix=None, code=None):
        self._command = _command
        self._parameters = _parameters
        # self.prefix: HpglCommand = prefix
        # self.suffix:HpglCommand = suffix

        if code is not None:
            self.decode(code)

        self._parameters = list(filter(("").__ne__, self._parameters)) #lehre stellen löschen

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
        if self._command == "XX":
            if self._parameters[0] == "13":
                return self._command + self._parameters[0] + "," + self._parameters[1]
            else:
                return self._command + self._parameters[0]
        elif self._command == "PB":
            return self._command + self._parameters[0]
        else:
            return self._command

    def get_parameters(self, typ=None):
        if self._command == "XX":
            ret = self._parameters[1:]
        elif self._command == "PB":
            ret = self._parameters[1:]
        else:
            ret = self._parameters
        this_typ = typ
        if this_typ is None:
            if self._command in HpglCommand.datatyp_dict:
                this_typ = HpglCommand.datatyp_dict[self._command]
            else:
                this_typ = [str, str, str, str, str, str]

        liste = []
        for val, type in zip(ret, this_typ):
            if type is int:
                liste.append(int(val))
            elif type is str:
                liste.append(str(val))
            elif type is float:
                liste.append(float(val))
        return liste


        # if this_typ is int:
        #     return [int(x) if x is not "" else x for x in ret]
        # elif this_typ is str:
        #     return [str(x) if x is not "" else x for x in ret]
        # elif this_typ is float:
        #     return [float(x) if x is not "" else x for x in ret]


    def set_parameter(self,data):
        str_data = [str(x) if x is not "" else x for x in data]
        if self._command == "XX":
            if self._parameters[0] == "13":
                str_data.insert(0, self._parameters[1])
                str_data.insert(0, self._parameters[0])
                self._parameters = str_data
            else:
                str_data.insert(0, self._parameters[0])
                self._parameters = str_data
        elif self._command == "PB":
            str_data.insert(0, self._parameters[0])
            self._parameters = str_data
        else:
            self._parameters = str_data


    def copy_from(self, parameter):
        self.__dict__.update(parameter.__dict__)

    def decode(self, string: str):
        m = re.findall(HpglCommand.re_patern, string) #regex
        if m is not None:
            res = m[0]
            self._command = res[0]
            li = [*res[1:]] #list umpacken sonst giebt es ein tupel-> schreibgeschützt
            # if li[0] is "": #das muss sein weil sonst bei __init__ gewisse stellen lehr bleiben
            #     li[0] = "0"
            # elif li[1] is "":
            #     li[1] = "0"
            # elif li[2] is "":
            #     li[2] = "0"
            self._parameters = li

    def encode(self):
        return self._command + ",".join(self._parameters) + ";"

    def assign_correction(self,offset: model_Offset):
        print(offset)

        pass



class Hpgl_structure:

    re_patern= "([A-Z]{2})([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?([-\d.]+)?[,;]?"
    # re_patern = "([A-Z]{2})(?:([-\d.]+)(?:,|;))+"

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

    def decode(self,data):
        matches = re.findall(Hpgl_structure.re_patern, data) #regex
        if len(matches) > 0:
            self.commands = []
            for m in matches:
                self.commands.append(HpglCommand(_command=m[0], _parameters=m[1:]))

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

    def assign_correction(self,offset: model_Offset.Offset):
        command_list = ["AA","PA","PD","PR","PU"]
        coammand: HpglCommand
        for coammand in self.commands:
            if coammand.get_command() in command_list:
                nx, ny =offset.assign_offset(coammand.get_parameters()[0],
                                             coammand.get_parameters()[1])
                # print(f"{coammand.get_command()} {int(nx*100)}, {int(ny*100)}")
                #coammand.get_parameters()[0] = int(nx*100) # ich weis nicht wiso das jemals funktioniert haben soll
                #coammand.get_parameters()[1] = int(ny*100)
                coammand.set_parameter([nx, ny])
        pass


if __name__ == "__main__":
    test = HpglCommand(code="XX13,1")
    print(test.__dict__)