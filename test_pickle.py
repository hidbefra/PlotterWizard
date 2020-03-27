import pickle

class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add (self):
        return self.a+self.b


test1 = test(3,4)
print(test1.add())

pickle_out = open("dict.pickle","wb")
pickle.dump(test1, pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle","rb")
test2 = pickle.load(pickle_in)
print(test2.add())