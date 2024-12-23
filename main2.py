class K17_07:
  def __init__(self, a1="Харків", a2="Одеса"):
    self.p1 = a1
    self.p2 = a2
  pass

ob1 = K17_07("Київ", "Полтава")
ob2 = K17_07("Львів")
ob3 = K17_07()
print(ob1.p1, ob1.p2)
print(ob2.p1, ob2.p2)
print(ob3.p1, ob3.p2)