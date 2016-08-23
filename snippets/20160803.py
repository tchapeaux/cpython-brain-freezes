class Foo(object):
    def __init__(self, param=[]):
        self.param = param


f = Foo()
f.param.append(2)
del f

f2 = Foo([])
print f2.param
