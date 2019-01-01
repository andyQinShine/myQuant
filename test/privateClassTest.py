# encoding: UTF-8

class car():
    # 类的私有变量, 用__定义的变量
    __count = 0
    t = 1
    def __init__(self, name):
        self.name = name
        self.__count += 1
        car.__count += 1
        self.t += 9
        car.t += 1
        # self.aaa = 1

    def __getattr__(self, name):
        print "You use getattr " + name
        return ""

    def __setattr__(self, name, value):
        print "You use setattr"
        self.__dict__[name] = value

    # def __getattribute__(self, name):
    #     print "you are useing getattribute"
    #     return object.__getattribute__(self, name)


    def display(self):
        print("name:" + self.name
              + "-self t:" + str(self.t)
              + "-car t:" + str(car.t)
              + "-self count:" + str(self.__count)
              + "-car.__count:" + str(car.__count))

# car1 = car('benzi')
#
# print (car1.display())
car2 = car('bmw')


print (car2.display())

print(car2.aaa)
car2.aaa = 7
print(car2.aaa)
print car2.__dict__