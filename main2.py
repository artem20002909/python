class K18_04c:
    def __init__(self, a1):
        self.p1 = a1
    def __add__(self, a2):
        self.p1 = self.p1 + a2
    def __str__ (self):
        return '%s' % self.p1

ob1 = K18_04c(21)
ob1 + 15
print(ob1)
ob2 = K18_04c("...")
ob2 + "download"
print(ob2)
ob3 = K18_04c([19, 7, 12])
ob3 + [5, 9]
print(ob3)
