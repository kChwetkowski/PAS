import socket

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 2010

    hostname = input("Podaj nazwę hosta: ")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(hostname.encode(), (SERVER_HOST, SERVER_PORT))

        response, _ = client_socket.recvfrom(1024)
        print("Otrzymana odpowiedź od serwera:", response.decode())

    except socket.error as e:
        print(f"Błąd podczas komunikacji z serwerem: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
