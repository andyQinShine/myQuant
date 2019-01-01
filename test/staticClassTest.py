#encoding:utf-8

class staticMethod():
    @staticmethod
    def foo():
        print "this is static  method foo"

class classMethod():
    @classmethod
    def bar(cls):
        print "this is class method bar"
        print "bar() is part of class:", cls.__name__

if __name__ =="__main__":
    static_foo = staticMethod()
    static_foo.foo()
    staticMethod.foo()
    print "**********"
    class_bar = classMethod()
    class_bar.bar()
    classMethod.bar()