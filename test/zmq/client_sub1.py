# encoding: UTF-8

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
# 消息过滤
socket.setsockopt(zmq.SUBSCRIBE,'')
while True:
    response = socket.recv()
    print("response %s" %response)
