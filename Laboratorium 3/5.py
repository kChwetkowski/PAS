import socket

def udp_client(host="127.0.0.1", port=2901):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (host, port)
        print("Wpisz 'stop' aby wyjść.")
        while True:
            message = input(": ")
            client_socket.sendto(message.encode(), server_address)
            response, _ = client_socket.recvfrom(1024)
            print("Otrzymana odpowiedź od serwera:", response.decode())
            if message.lower() == "stop":
                break

    except socket.error as e:
        print("Wystąpił błąd podczas połączenia:", e)
    finally:
        client_socket.close()


if __name__ == "__main__":
    udp_client()
