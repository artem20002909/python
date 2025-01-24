import math

class K18_07a:
    def __init__(self, x):
        self.plcolo = 3.14 * x * x
class K18_07b:
    def __init__(self, x):
        self.pltrik = math.sqrt(3)
class K18_07:
    def __init__(self, x, y):
        self.plzag = x * y
    def func1(self, r1, r2, a, m=2, n=2):
        self.p1 = K18_07a(r1)
        self.p2 = K18_07a(r2)
        self.p3 = K18_07b(a)
        self.k1 = m
        self.k2 = n
    def func2(self):
        self.func2 = self.plzag - self.p1.plcolo * self.k1\
            -self.p2.plcolo * self.k2 - self.p3.pltrik
    def func3(self):
        print("загальна площя = ", str(self.plzag), "см.квадратних")
        print("залишок площі", str(self.func2), "см.квадратних")

ob = K18_07(30, 20)
ob.func1(4, 6, 5)
ob.func2()
ob.func3()
