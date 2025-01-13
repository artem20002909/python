class K17_10:
    def __init__(self , a1, a2, a3):
        self.p1 = a1
        self.p2 = a2
        self.p3 = a3
        self.funcl ()
    def funcl(self):
        s = (self.p2*self.p3)/2
        print(self.p1, s)

ob1 = K17_10("площя 1 = ", 3, 4)
ob2 = K17_10("площя 2=", 5, 6)
ob1.form = "перший зафарбований"
print(ob1.form)
