import time
import grpc
import sys
import drone_pb2
import drone_pb2_grpc

from concurrent import futures

count = 0
drones = {}
limit = 2


class DroneServer(drone_pb2_grpc.MoveDroneServicer):

    def move(self, request, context):
        global count
        tmp1 = sys.argv[1]
        tmp2 = sys.argv[2]
        if count == 0:
            count = 1
            i = count - 1
            response = drone_pb2.Response(num=count, coords=tmp1, mode='M')
            yield response
            drones[i] = {'ID': count, 'Coordinates': tmp1}
            print('Following Client has joined:', drones[i])
            count += 1
        else:
            response = drone_pb2.Response(num=count, coords=tmp2, mode='M')
            yield response
            i = count - 1
            drones[i] = {'ID': count, 'Coordinates': tmp2}
            print('Following Client has joined:', drones[i])
            count += 1
        if count > limit:
            tmp = input('Enter New Coordinates [x,y,z]:')
            tmp1 = tmp.split(',')
            for i in range(len(drones)):
                d = drones[i]
                c = d['Coordinates']
                c1 = c.split(',')
                c1[0] = int(c1[0]) + int(tmp1[0])
                c1[1] = int(c1[1]) + int(tmp1[1])
                c1[2] = int(c1[2]) + int(tmp1[2])
                c = str(str(c1[0]) + ',' + str(c1[1]) + ',' + str(c1[2]))
                d['Coordinates'] = c
                drones[i] = d
                response = drone_pb2.Response(num=d['ID'], coords=d['Coordinates'], mode='A')
                yield response


def run(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drone_pb2_grpc.add_MoveDroneServicer_to_server(DroneServer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            print("Server started at %d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 3000)
