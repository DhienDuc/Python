class Base:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def Show(self):
        print(self.fname, self.lname)

class Vo(Base):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    


A = Vo("Vu Thi", "Xuan")
A.Show()
