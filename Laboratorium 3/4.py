import socket


def udp_client(host="127.0.0.1", port=2901, message="Hello, server!"):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(message.encode(), (host, port))
        response, _ = client_socket.recvfrom(1024)
        print("Otrzymana odpowiedź od serwera:", response.decode())

    except socket.error as e:
        print("Wystąpił błąd podczas połączenia:", e)
    finally:
        client_socket.close()


if __name__ == "__main__":
    udp_client()
