import socket
import sys

def connect_to_server(server_address, server_port):
    try:
        server_ip = socket.gethostbyname(server_address)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  #timeout na 5s
            s.connect((server_ip, server_port))
            return True
    except Exception as e:
        print(f"Wystąpił błąd podczas łączenia z serwerem: {e}")
        return False


def main():
    server_address = input("Podaj adres serwera: ")
    server_port = int(input("Podaj port: "))

    if connect_to_server(server_address, server_port):
        print("Połączenie z serwerem udane.")
    else:
        print("Nie udało się nawiązać połączenia z serwerem.")

if __name__ == "__main__":
    main()
