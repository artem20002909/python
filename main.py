class K18_16:
    def __init__(self, a1, a2):
        try:
            self.z = a1 / a2
        except ZeroDivisionError:
            print("0")
        else:
            print("result=", self.z)
        finally:
            print("program stop")

x = int(input("x"))
v = int(input("v"))
