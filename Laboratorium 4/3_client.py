import socket

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 2010

    message = "Hello server!"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
        print(f"Wysłano wiadomość do serwera ({SERVER_HOST}:{SERVER_PORT}): {message}")

        response, _ = client_socket.recvfrom(1024)
        print("Odebrano odpowiedź od serwera:", response.decode())
    except socket.error as e:
        print(f"Błąd podczas komunikacji z serwerem: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
