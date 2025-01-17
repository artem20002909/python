class K17_12:
  contr = int(input("mass :"))
  def __init__(self, a1, a2, a3):
    self.p1 = a1
    self.p2 = a2
    self.p3 = a3
  def func1(self):
    v = self.p1 * self.p2 * self.p3
    print("ob`em", m, " =", v)

class K17_12a(K17_12):
  def func2(self, vaga):
    if vaga < K17_12.contr:
      self.p4 = "mojno "
    else:
      self.p4 = " ne mojno:("
  def func3(self):
    print(self.p4)

ob1 = K17_12a(2, 3, 4)
m = "1"
ob1.func1()
ob2 = K17_12(3, 4, 5)
m = "2"
ob2.func1()
ob1.func2(5)
ob1.func3()
