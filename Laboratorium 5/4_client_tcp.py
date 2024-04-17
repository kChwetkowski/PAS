import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

MESSAGE = b"testowawiadomosc1234567890"

start_time = time.time()
for _ in range(200000):
    client_socket.sendall(MESSAGE)
    data = client_socket.recv(1024)
end_time = time.time()

client_socket.close()

print("Otrzymano:", data.decode())
print("Czas przesyłu TCP:", end_time - start_time, "sekund")
