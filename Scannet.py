import socket
import sys

if len(sys.argv) < 2:
    print('Set host ip.: {} 127.0.0.1'.format(sys.argv[0]))
    exit(0)

target = sys.argv[1]
print('scanming host with ip{} '.format(target))

for port in range(1, 200):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target,port))
    if result == 0:
        print('port {} is open'.format(port))
    ##else result == 1: 
        ##print('port {} is close'.format(port))
