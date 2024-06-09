import socket


def main():
    server_address = ('127.0.0.1', 12345)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    print("Połączono z serwerem.")

    try:
        while True:
            message = input("Wpisz wiadomość: ")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)

            print("Odpowiedź od serwera:", data.decode())
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
