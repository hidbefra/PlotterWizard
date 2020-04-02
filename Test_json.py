import json
from typing import List
import myJson

class elter():
    def __init__(self,a):
        self.a = a
        print("constructor elter")


class test(elter):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
        print("constructor test")

class container():
    def __init__(self):
        self.cont: List[kecks] = []
        self.cont.append(kecks("Bäretätzli"))

class schogi():
    def __init__(self, typ):
        self.typ = typ
        self.geheim = "kroete"

class inhalt():
    def __init__(self, zutat: str):
        self.zutat: List[schogi]= []
        self.zutat.append(schogi(zutat + " salz"))
        self.zutat.append(schogi(zutat + " pfefer"))
        self.schogi = schogi(zutat)


class kecks():
    def __init__(self,kecks: str):
        self.kecks = kecks
        self.name = "Kruemonster"
        self.inhalt = inhalt("kako")




t = test(1,2)

cont = container()

myobj_keks = kecks("guzli")


myJsonData = json.dumps(myobj_keks, indent=4, cls=myJson.MyJsonEncoder)

myJsonData = myJson.dumps(myobj_keks)

print(myJsonData)

testKeks: kecks = myJson.loads(myJsonData,kecks)

print(testKeks.inhalt.zutat[1].typ)




