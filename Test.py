
class elter():
    def __init__(self):
        print("constructor elter")


class test(elter):
    def __init__(self):
        super().__init__()
        print("constructor test")


    def m(self,i):
        if type(i) is int:
            print("int")
        if type(i) is str:
            print("str")



t = test()
t.m(1)
t.m("hallo")