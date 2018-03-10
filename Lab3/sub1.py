import sys
import zmq

port = "5559"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print("Collecting updates from server...")
socket.connect ("tcp://localhost:%s" % port)
socket.setsockopt_string(zmq.SUBSCRIBE, '')

socket1 = context.socket(zmq.PUB)
port = "5560"
socket1.connect("tcp://localhost:%s" % port)

while True:
    try:
        string = socket.recv()
        string = string.decode()
        topic = string.split()
        print(topic)
        socket1.send_string("%s" % topic)
    except KeyboardInterrupt:
        sys.exit()
