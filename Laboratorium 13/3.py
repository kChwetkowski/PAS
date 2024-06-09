import socket
import threading
import os

class FileDownloadServer:
    def __init__(self, host='127.0.0.1', port=6666, files_dir='images'):
        self.host = host
        self.port = port
        self.files_dir = files_dir
        os.makedirs(self.files_dir, exist_ok=True)

    def handle_client(self, connection, address):
        print(f"Połączenie z {address}")
        try:
            command = connection.recv(1024).decode('utf-8').strip()
            if command == 'GET_IMAGE':
                filename = 'example_image.jpg'  # przykładowy plik
                filepath = os.path.join(self.files_dir, filename)
                if os.path.exists(filepath):
                    filesize = os.path.getsize(filepath)
                    connection.sendall(f'SIZE {filesize} NAME {filename} \r\n'.encode('utf-8'))
                    with open(filepath, 'rb') as f:
                        connection.sendall(f.read())
                else:
                    connection.sendall(b'ERROR \r\n')
            else:
                connection.sendall(b'ERROR \r\n')
        except Exception as e:
            print(f"Błąd: {e}")
        finally:
            connection.close()
            print(f"Połączenie z {address} zakończone")

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Serwer nasłuchuje na {self.host}:{self.port}")
        while True:
            connection, address = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(connection, address))
            client_thread.start()

if __name__ == '__main__':
    server = FileDownloadServer()
    server.run()
