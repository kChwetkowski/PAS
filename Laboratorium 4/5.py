import socket

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 2010

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((SERVER_HOST, SERVER_PORT))

        print("Serwer UDP nasłuchuje na porcie", SERVER_PORT)

        while True:
            data, client_address = server_socket.recvfrom(1024)
            client_ip = data.decode()

            try:
                hostname = socket.gethostbyaddr(client_ip)[0]
                response = f"Adres IP: {client_ip}, Hostname: {hostname}"
            except socket.herror:
                response = f"Nie można znaleźć nazwy hosta dla adresu IP: {client_ip}"

            server_socket.sendto(response.encode(), client_address)
            print(f"Odpowiedź wysłana do klienta {client_address}")

    except socket.error as e:
        print(f"Błąd podczas działania serwera: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
