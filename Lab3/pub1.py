import zmq
import sys
import threading
import time

name = sys.argv[1]
port = "5559"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:%s" % port)
print("User[%s] Connected to the chat server." % name)

socket1 = context.socket(zmq.SUB)
port = "5560"
socket1.connect("tcp://localhost:%s" % port)
socket1.setsockopt_string(zmq.SUBSCRIBE, '')


def print_sent_msg():
    text = input("[%s]: " % name)
    socket.send_string("[%s]:%s" % (name,text))


def print_received_message():
    while True:
        string = socket1.recv()
        string = string.decode()
        print(string)


if __name__ == "__main__":
    receiver = threading.Thread(target=print_received_message)
    receiver.Daemon = True
    receiver.start()
    print_sent_msg()
    print_received_message()
    time.sleep(1)
