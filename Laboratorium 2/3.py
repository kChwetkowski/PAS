import socket

def tcp_client(host="127.0.0.1", port=2900):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Wpisz 'stop' aby wyjść.")
        while True:
            message = input(": ")
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024)
            print("Otrzymana odpowiedź od serwera:", response.decode())
            if message.lower() == "stop":
                break

    except socket.error as e:
        print("Wystąpił błąd podczas połączenia:", e)
    finally:
        client_socket.close()


if __name__ == "__main__":
    tcp_client()
