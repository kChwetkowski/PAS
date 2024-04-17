import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print("Serwer UDP nasłuchuje na porcie", UDP_PORT)

while True:
    data, address = server_socket.recvfrom(1024)
    if not data:
        break
    server_socket.sendto(data, address)
