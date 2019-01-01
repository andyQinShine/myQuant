#coding = utf-8

"""
study __getattr__ and __setattr__
"""

class Rectangle(object):
    """
        the width and length of Rectangle
    """

    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

    def __setattr__(self,name, value):
        if name == "size1":
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == "size1":
            return self.width, self.height
        else:
            raise AttributeError

def foo(num,str):
    name = "qiwsr"
    print locals()
    print globals()

if __name__ == "__main__":
    r = Rectangle()
    r.width = 3
    r.height = 4
    print r.size
    r.size = 30, 40
    print r.width
    print r.height

    print r.size1
    r.size1 = 40,70
    print r.size1

    print r.__class__
    print type(r)
    print r
    print ("----------------------------------")
    print dir(r)

    print ("----------------------------------")
    foo(221,'github')
