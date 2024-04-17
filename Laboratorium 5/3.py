import socket

SERVER_ADDRESS = '127.0.0.1'
TCP_PORT = 2011
PING_PORTS = [5666, 1234, 6666, 7666, 8666, 1024, 1022]


def knock_ports():
    try:
        for port in PING_PORTS:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.sendto(b'PING', (SERVER_ADDRESS, port))
            response, _ = client_socket.recvfrom(1024)
            if response == b'PONG':
                print(f"Port {port} otwarty.")
            else:
                print(f"Port {port} zamknięty.")
            client_socket.close()
    except Exception as e:
        print("Wystąpił błąd podczas knockowania portów:", e)


def main():
    try:
        knock_ports()
        tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client_socket.connect((SERVER_ADDRESS, TCP_PORT))
        received_data = tcp_client_socket.recv(1024)
        print("Otrzymano wiadomość od serwera:", received_data.decode())
        tcp_client_socket.close()
    except Exception as e:
        print("Wystąpił błąd podczas komunikacji z serwerem:", e)


if __name__ == "__main__":
    main()
