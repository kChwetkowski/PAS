import socket
from datetime import datetime

def main():
    HOST = '127.0.0.1'
    PORT = 2010

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print("Serwer jest gotowy do przyjmowania połączeń...")

        while True:
            client_socket, client_address = server_socket.accept()
            print("Połączenie nawiązane z", client_address)
            message = client_socket.recv(1024).decode()
            print("Wiadomość od klienta:", message)
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            client_socket.sendall(current_datetime.encode())
            client_socket.close()

    except Exception as e:
        print("Wystąpił błąd:", e)

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
