import socket

def main():
    HOST = '127.0.0.1'
    PORT = 2010

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print("Serwer UDP oczekuje na połączenia...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Otrzymano wiadomość od klienta {client_address}: {data.decode()}")

        server_socket.sendto(data, client_address)
        print("Odebrana wiadomość została odesłana do klienta.")

if __name__ == "__main__":
    main()
