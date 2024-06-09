import socket
import os


class FileUploadClient:
    def __init__(self, server_host='127.0.0.1', server_port=6666):
        self.server_host = server_host
        self.server_port = server_port

    def upload_file(self, file_path):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.server_host, self.server_port))
                client_socket.sendall(b'UPLOAD\n')
                filename = os.path.basename(file_path)
                filename_length = len(filename)
                client_socket.sendall(filename_length.to_bytes(2, byteorder='big'))
                client_socket.sendall(filename.encode('utf-8'))
                filesize = os.path.getsize(file_path)
                client_socket.sendall(filesize.to_bytes(8, byteorder='big'))
                with open(file_path, 'rb') as f:
                    client_socket.sendall(f.read())
                response = client_socket.recv(1024).decode('utf-8')
                if response == 'UPLOAD_SUCCESS':
                    print("Plik został pomyślnie przesłany")
                else:
                    print("Błąd przy przesyłaniu pliku")
        except Exception as e:
            print(f"Błąd: {e}")


if __name__ == '__main__':
    client = FileUploadClient()
    client.upload_file('image.png')
