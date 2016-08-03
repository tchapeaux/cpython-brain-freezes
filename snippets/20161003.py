class Foo(object):
    def __init__(self, param=None):
        self.param = param if param is not None else []


f = Foo()
f.param.append(2)
del f

f2 = Foo([])
print f2.param
