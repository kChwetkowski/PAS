import socket

class FileDownloadClient:
    def __init__(self, server_host='212.182.24.27', server_port=2904):
        self.server_host = server_host
        self.server_port = server_port

    def download_file(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.server_host, self.server_port))
                client_socket.sendall(b'GET_IMAGE \r\n')
                header = client_socket.recv(1024).decode('utf-8').strip()
                if header.startswith('SIZE'):
                    parts = header.split()
                    size = int(parts[1])
                    name = parts[3]
                    file_data = client_socket.recv(size)
                    with open(name, 'wb') as f:
                        f.write(file_data)
                    print(f"Pobrano plik: {name}")
                else:
                    print("Błąd serwera")
        except Exception as e:
            print(f"Błąd: {e}")

if __name__ == '__main__':
    client = FileDownloadClient()
    client.download_file()
