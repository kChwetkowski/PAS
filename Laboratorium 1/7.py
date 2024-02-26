import socket
import sys


def scan_ports(server_address):
    open_ports = []
    try:
        ip = socket.gethostbyname(server_address)
        print(f"Skanowanie portów dla hosta: {server_address} ({ip})")
    except socket.gaierror:
        print("Nieprawidłowy adres IP lub nazwa hosta.")
        return open_ports


    port_range = range(1, 1025)  # Porty <1;1024>

    for port in port_range:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except KeyboardInterrupt:
            print("\nSkanowanie przerwane przez użytkownika.")
            sys.exit()
        except socket.error:
            print("Nie można połączyć się z serwerem.")
            sys.exit()

    return open_ports


def main():
    server_address = input("Podaj adres serwera: ")
    open_ports = scan_ports(server_address)

    if open_ports:
        print("Otwarte porty:")
        for port in open_ports:
            print(f"Port {port} jest otwarty.")
    else:
        print("Nie znaleziono otwartych portów.")
    input("")

if __name__ == "__main__":
    main()
