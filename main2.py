class K18_06:
    def __init__(self, a1, a2):
        self.p1 = a1
        self.p2 = a2
    def func1(self):
        self.p1 =self.p1 / self.p2
        print(self.p1)

class K18_06a(K18_06):
    def func1(self):
        print("перехід 1")
        K18_06.func1(self)
        print("перехід 2")

i = 1
while i < 7:
    if 2 < i and i < 5:
        ob1 = K18_06a(7, i)
    else:
        ob1 = K18_06(10, i)
    i += 1
    ob1.func1()
