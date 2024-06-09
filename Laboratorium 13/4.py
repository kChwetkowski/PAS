import socket

class FileDownloadClient:
    def __init__(self, server_host='127.0.0.1', server_port=6666):
        self.server_host = server_host
        self.server_port = server_port

    def list_files(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.server_host, self.server_port))
                client_socket.sendall(b'LIST_FILES \r\n')
                files = client_socket.recv(1024).decode('utf-8').strip()
                print("Dostępne pliki: ", files)
        except Exception as e:
            print(f"Błąd: {e}")

    def download_file(self, filename):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.server_host, self.server_port))
                client_socket.sendall(f'GET_IMAGE {filename} \r\n'.encode('utf-8'))
                header = client_socket.recv(1024).decode('utf-8').strip()
                if header.startswith('SIZE'):
                    parts = header.split()
                    size = int(parts[1])
                    file_data = client_socket.recv(size)
                    with open(filename, 'wb') as f:
                        f.write(file_data)
                    print(f"Pobrano plik: {filename}")
                else:
                    print("Błąd serwera")
        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == '__main__':
    client = FileDownloadClient()
    client.list_files()
    client.download_file('example_image.jpg')
