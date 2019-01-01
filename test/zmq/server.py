# encoding: UTF-8

import zmq
from datetime import datetime
import time

context = zmq.Context()
# socket = context.socket(zmq.REP)
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    # message = socket.recv()
    # print ("Received: %s" %message)
    # socket.send("I am OK")

    print ("send message")
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    socket.send("系统广播, %s" %now)
    time.sleep(10)
