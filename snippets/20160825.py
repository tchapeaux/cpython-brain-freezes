class Foo(object):
    def __init__(self):
        self.foo = 3
        self.consistency_check()

    def consistency_check(self):
        assert self.foo == 3


class Bar(Foo):
    def __init__(self):
        super(Bar, self).__init__()
        self.bar = 2
        self.consistency_check()

    def consistency_check(self):
        Foo.consistency_check(self)
        assert self.bar == 2

a = Foo()
print a

b = Bar()
print b
