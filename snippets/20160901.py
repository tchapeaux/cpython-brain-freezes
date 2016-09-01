def default_callback():
        print "bar was fooed or whatever"


class Foo(object):
    def __init__(self, mything, mycallback=None):
        self.mything = mything
        if mycallback is None:
            self.post_bar = default_callback
        else:
            self.post_bar = mycallback

    def bar(self, vil):
        print self.mything, vil
        self.post_bar()



a = Foo(3)
a.bar("licorice")

def zandog():
    print "YOU GOT HACKED"

a = Foo(53, mycallback=zandog)
a.bar("vanilla")
