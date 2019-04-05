class base(object):

    def __init__(self):
        print "Base"

class child(base):

    def __init__(self):
        super(child, self).__init__()
        print "Child"

c = child()