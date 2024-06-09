import socket
import threading
import logging
from datetime import datetime

logging.basicConfig(filename='server_log.txt', level=logging.INFO)


class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address

    def run(self):
        logging.info(f"Połączenie z {self.address} rozpoczęte o {datetime.now()}")
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            self.connection.sendall(data)
        self.connection.close()
        logging.info(f"Połączenie z {self.address} zakończone o {datetime.now()}")


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(5)
        logging.info(f"Serwer nasłuchuje na {self.ip}:{self.port} o {datetime.now()}")

        while True:
            connection, address = server_socket.accept()
            client_thread = ClientThread(connection, address)
            client_thread.start()


if __name__ == '__main__':
    server = Server('127.0.0.1', 6666)
    server.run()
