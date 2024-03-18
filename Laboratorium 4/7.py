import socket

def tcp_client(host="127.0.0.1", port=2900, message="Hello, server!"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        truncated_message = message[:20]
        client_socket.sendall(truncated_message.encode())
        response = client_socket.recv(1024)
        print("Otrzymana odpowiedź od serwera:", response.decode())

    except socket.error as e:
        print("Wystąpił błąd podczas połączenia:", e)
    finally:
        client_socket.close()


if __name__ == "__main__":
    tcp_client()
