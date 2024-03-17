import socket
import sys
from time import gmtime, strftime


def check_msg_syntax(txt):
    txt = txt.decode()
    s = txt.split(";")
    if len(s) != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad14odp" and tmp[1] == "src" and tmp[3] == "dst" and tmp[5] == "data":
            try:
                src_port = int(tmp[2])
                dst_port = int(tmp[4])
                data = tmp[6]
            except ValueError:
                return "BAD_SYNTAX"
            if src_port == 60788 and dst_port == 2901 and data == "programming in python is fun":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"


HOST = '127.0.0.1'
PORT = 2911

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except OSError as e:
    print('Bind failed. Error Code : ' + str(e.errno) + ' Message: ' + e.strerror)
    sys.exit()

print("[%s] UDP ECHO Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime()))

try:
    while True:

        data, address = sock.recvfrom(1024)
        print('[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data))

        if data:
            answer = check_msg_syntax(data)
            sent = sock.sendto(answer.encode(), address)
            print('[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address))
finally:
    sock.close()
