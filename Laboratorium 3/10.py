import socket

def main():
    server_address = '127.0.0.1'
    server_port = 2907

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        client_hostname = socket.gethostname()
        client_socket.sendto(client_hostname.encode(), (server_address, server_port))
        server_response, _ = client_socket.recvfrom(1024)
        server_ip = server_response.decode()
        print(f"Odpowiedź serwera: {server_ip}")

    except socket.error as e:
        print(f"Błąd połączenia: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
