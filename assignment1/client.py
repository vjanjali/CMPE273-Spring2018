import grpc, time, sys
import drone_pb2_grpc
import drone_pb2

drones = {}


def move_stub(response):
    global i
    i = 0
    for r in response:
        print('Client ID: ', r.num, 'connected to server')
        print('received ', r.coords)
        print('moving to ', r.coords)
        drones[i] = {'ID': r.num, 'Coordinates': r.coords}
        print(drones[i])
        i += 1


def adjust_stub(r):
    print('received ', r.coords)
    print('moving to ', r.coords)
    d = {'ID': r.num, 'Coordinates': r.coords}
    print(d)


def run():
    channel = grpc.insecure_channel('localhost:3000')
    stub = drone_pb2_grpc.MoveDroneStub(channel)
    response = stub.move(drone_pb2.Request())
    move_stub(response)
    for r in response:
        if r.mode == 'A':
            adjust_stub(response)
    while True:
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    run()
