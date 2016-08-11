try:
    print "hello"
    raise Exception("oh no")
    print "bye"
except Exception:
    print "Sorry"
    raise
finally:
    print "Oh well"
