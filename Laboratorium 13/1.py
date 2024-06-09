import socket
import threading
import os


class FileUploadServer:
    def __init__(self, host='127.0.0.1', port=6666, save_dir='uploads'):
        self.host = host
        self.port = port
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

    def handle_client(self, connection, address):
        print(f"Połączenie z {address}")
        try:
            while True:
                command = connection.recv(7).decode('utf-8')
                if command == 'UPLOAD\n':
                    filename_length = int.from_bytes(connection.recv(2), byteorder='big')
                    filename = connection.recv(filename_length).decode('utf-8')
                    filesize = int.from_bytes(connection.recv(8), byteorder='big')
                    filepath = os.path.join(self.save_dir, filename)
                    with open(filepath, 'wb') as f:
                        remaining = filesize
                        while remaining > 0:
                            chunk_size = 4096 if remaining >= 4096 else remaining
                            chunk = connection.recv(chunk_size)
                            if not chunk:
                                break
                            f.write(chunk)
                            remaining -= len(chunk)
                    connection.sendall(b'UPLOAD_SUCCESS')
                else:
                    connection.sendall(b'INVALID_COMMAND')
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
    server = FileUploadServer()
    server.run()
