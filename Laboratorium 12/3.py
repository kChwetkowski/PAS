import socket
import threading
import random


class ClientThread(threading.Thread):
    def __init__(self, connection, address, secret_number):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.secret_number = secret_number

    def run(self):
        print(f"Połączenie z {self.address} rozpoczęte")
        self.connection.sendall(b"Zgadnij liczbe od 1 do 100: ")
        while True:
            data = self.connection.recv(1024).strip()
            if not data:
                break
            try:
                guess = int(data.decode('ascii'))
                if guess < self.secret_number:
                    self.connection.sendall(b"Za malo\n")
                elif guess > self.secret_number:
                    self.connection.sendall(b"Za duzo\n")
                else:
                    self.connection.sendall(b"Gratulacje! Zgadles!\n")
                    break
            except ValueError:
                self.connection.sendall(b"To nie jest liczba. Prosze sprobowac ponownie.\n")
        self.connection.close()
        print(f"Połączenie z {self.address} zakończone")


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(5)
        print(f"Serwer nasłuchuje na {self.ip}:{self.port}")

        while True:
            connection, address = server_socket.accept()
            secret_number = random.randint(1, 100)
            client_thread = ClientThread(connection, address, secret_number)
            client_thread.start()


if __name__ == '__main__':
    server = Server('127.0.0.1', 6666)
    server.run()
