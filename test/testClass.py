import json
from datetime import datetime
class testHello():
    def __init__(self):
        self.base = "eos";
        self.quote = "btc";
        self.symbol = self.base + self.quote
        self.list = ['a', 'b', 'c', {'now' : str(datetime.now())}]


if __name__ == '__main__':
    # hello = testHello();
    # print(hello.symbol)
    # print(json.dumps(hello.list))
    # print ("stop is " + str(True))
    # obj = {"a" : 5}
    # print ("obj is " + obj)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print (now)