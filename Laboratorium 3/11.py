import socket

def main():
    server_address = '127.0.0.1'
    server_port = 2908

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_address, server_port))
        message = input("Wprowadź wiadomość: ")
        if len(message) < 20:
            message += ' ' * (20 - len(message))
        elif len(message) > 20:
            message = message[:20]
        client_socket.sendall(message.encode())

        server_response = client_socket.recv(1024)
        print("Odpowiedź od serwera:", server_response.decode())

    except socket.error as e:
        print("Błąd połączenia:", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
