import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address

    def run(self):
        print(f"Połączenie z {self.address} rozpoczęte")
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            self.connection.sendall(data)
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
            client_thread = ClientThread(connection, address)
            client_thread.start()

if __name__ == '__main__':
    server = Server('127.0.0.1', 6666)
    server.run()
