class K18_04:
    def __init__(self, a1):
        self.p = a1
    def func1(self):
        print("K18_04 =", self.p - 13)

class K18_04a(K18_04):
    def func2(self, a2):
        self.p *= a2
        print("K18_04a =", self.p)

class K18_04b(K18_04):
    def func3(self):
        self.func3 = list(str(self.p))
        print("list=", self.func3)
    def func1(self):
        i = 0
        while i < len(self.func3):
            print(i, "element:", self.func3[i])
            i += 1

ob1 = K18_04a(37)
ob2 = K18_04b('byte')
ob1.func2(3)
ob1.func1()
ob2.func3()
ob2.func1()
