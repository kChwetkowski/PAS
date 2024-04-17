import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MESSAGE = b"testowawiadomosc1234567890"

start_time = time.time()
for _ in range(200000):
    client_socket.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data, _ = client_socket.recvfrom(1024)
end_time = time.time()

client_socket.close()

print("Otrzymano:", data.decode())
print("Czas przesyłu UDP:", end_time - start_time, "sekund")
