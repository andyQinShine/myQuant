import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send("Are you OK?")
response = socket.recv()
print ("response %s" %response)