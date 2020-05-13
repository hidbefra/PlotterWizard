import json
from typing import List
import my_Json
import model_Schnittparameter
from model_Hpgl import *


class elter():
    def __init__(self,a):
        self.a = a
        print("constructor elter")


class kind(elter):
    def __init__(self,json=None,a=None,b=None):
        if (json==None):
            super().__init__(a)
            self.b = b
            print("constructor kind")
        else:
            self.__dict__ = json


class container():
    def __init__(self):
        self.cont: List[kecks] = []
        self.cont.append(kecks("Bäretätzli"))

class schogi():
    def __init__(self, typ):
        self.name ="test"
        self.typ = typ
        self.geheim = "kroete"

class inhalt():
    def __init__(self, zutat: str):
        self.zutat: List[schogi]= []
        self.zutat.append(schogi(zutat + " salz"))
        self.zutat.append(schogi(zutat + " pfefer"))
        self.schogi = schogi(zutat)


class kecks():

    anzahl = 1

    def __init__(self,json = None):
        print("Kecks construcktor")
        kecks.anzahl += 1
        if (json==None):
            self.name = "my kecks"
        else:
            self.__dict__ = json



class lecker():
    def __init__(self,json = None):
        print("lecker construcktor")
        if (json==None):
            self.name = "my lecker"
            self.anzahl = 5
            self.container: List[kecks] = []
        else:
            self.__dict__ = json

    def import_from_json(self, json):
        self.__dict__ = json

    def __iter__(self):
        yield ()


# t = test(1,2)
#
# cont = container()
#
# myobj_keks = kecks("guzli")
#
#
# myJsonData = json.dumps(myobj_keks, indent=4, cls=my_Json.MyJsonEncoder)
#
# myJsonData = my_Json.dumps(myobj_keks)
#
# print(myJsonData)
#
# testKeks: kecks = my_Json.loads(myJsonData, kecks)
#
# print(testKeks.inhalt.zutat[1].typ)
# print(testKeks.anzahl)

# snp= model_Schnittparameter.Schnittparameter()
# myJsonData = my_Json.dumps(snp)
# print(myJsonData)
# spn2 = my_Json.loads(myJsonData, kecks)
# print(spn2.name)

# snp = lecker()
# snp.name = "Humbel"
# snp.anzahl = 389898
# ke = kecks()
# ke.name = "Brunzli"
# snp.container.append(ke)
# myJsonData = my_Json.dumps(snp)
# print(snp.__dict__)
# print(myJsonData)
# spn2: lecker = my_Json.loads(myJsonData, lecker)
# print(spn2.name)
# print(spn2.anzahl)
# print(spn2.container[0].name)
# print(kecks.anzahl)
#
# k = kind(None,1,2)
# myJsonData = my_Json.dumps(k)
# print(myJsonData)
# k2: kind = my_Json.loads(myJsonData, kind)
# print(k2.a)
# print(k2.b)


class Zeugniss:
    def __init__(self, note: int = None):
        print("const Zeugniss")
        self.note = note
        pass

class Fach:
    def __init__(self,name = None):
        self.name = name

class Lehrer:
    def __init__(self, name: str = None, fach = None):
        print("const Lehrer")
        self.name = name

        if isinstance(fach[0], dict):
            self.fach = []
            for le in fach:
                self.fach.append(Fach(**le))

        if isinstance(fach[0], Fach):
            self.fach = fach

class Student:
    def __init__(self, first_name: str = None, last_name:  str = None, zeugniss=None, fächer=None, lehrer=None):
        print("const Student")
        self.first_name = first_name
        self.last_name = last_name

        # für klasse
        if zeugniss is None:
            self.zeugniss = Zeugniss()
        elif isinstance(zeugniss, dict):
            self.zeugniss.__init__(**zeugniss)
        elif isinstance(zeugniss, Zeugniss):
            self.zeugniss = zeugniss
        # init_class(self.zeugnis, Zeugniss, zeugniss)

        # für Variable
        self.fächer = fächer

        # für Listen von klassen
        if lehrer is None:
            self.lehrer = []
        elif isinstance(lehrer[0], dict):
            self.lehrer = []
            for le in lehrer:
                self.lehrer.append(Lehrer(**le))
        elif isinstance(lehrer[0], Lehrer):
            self.lehrer = lehrer


def init_class(objekt, _class, daten):
    if daten is None:
        objekt = _class()
    elif isinstance(daten, dict):
        objekt.__init__(**daten)
    elif isinstance(objekt, _class):
        objekt = daten

fach = [Fach("musik"),Fach("sex")]

c1 = HpglCommand("PD", [1000,1000])
c2 = HpglCommand("PU", [333,333])
c3 = HpglCommand("NR",prefix=c1,suffix=c2)

fächer=[c1,c2,c3]

lehrer=[Lehrer("Paul Peter",fach),Lehrer("Fredy",fach)]

student = Student(first_name="Jake", last_name="Doyle",zeugniss=Zeugniss(6),fächer=fächer, lehrer=lehrer)

json_data = my_Json.dumps(student)
# json_data = json.dumps(student.__dict__)
print(json_data)
st: Student = Student(first_name="nüt", last_name="öpis")
st.__init__(**my_Json.loads(json_data))
print(st.zeugniss.note)
print(*st.fächer)

le: Lehrer
fa: Fach
for le in st.lehrer:
    for fa in le.fach:
        print(f"{le.name} {fa.name}")

a = {"test": Hpgl_structure("LL")}
print(a["test"].code)