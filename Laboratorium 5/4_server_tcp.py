import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1)

print("Serwer TCP nasłuchuje na porcie", TCP_PORT)

while True:
    connection, address = server_socket.accept()
    print("Połączono z klientem:", address)
    while True:  # Obsługa wielu wiadomości bez zamykania połączenia
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
    connection.close()
