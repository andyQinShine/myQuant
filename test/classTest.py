class dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def eat(self, food):
        print self.name  + ' eat ' + food

    def run(self, place):
        self.eat("eat")
        print self.name + ' runing ' + place

class Jiwawa(dog):
    def __init__(self, name, color, age):
        super(Jiwawa, self).__init__(name, color)
        self.age = age

    def eat(self, food):
        print self.name + ' is my dog, she is eating ' + food

if __name__ == '__main__':
    mydog = Jiwawa('jiwawa', 'yellow', 25)
    mydog.run('caochang')