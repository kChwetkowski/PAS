import socket

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 2010

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((SERVER_HOST, SERVER_PORT))

        print("Serwer nasłuchuje na porcie UDP", SERVER_PORT)

        while True:
            data, client_address = server_socket.recvfrom(1024)
            hostname = data.decode()

            try:
                ip_address = socket.gethostbyname(hostname)
                response = ip_address.encode()
            except socket.error as e:
                response = f"Błąd: {e}".encode()

            server_socket.sendto(response, client_address)
            print(f"Odesłano odpowiedź do klienta {client_address}: {response.decode()}")

    except socket.error as e:
        print(f"Błąd podczas obsługi serwera: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
