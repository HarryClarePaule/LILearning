class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B): # this order wil determine what name will be printed. A before B means "Class A" will be printed. See "mro" message below
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.showprops()
print(C.__mro__) # mro - message resolution order