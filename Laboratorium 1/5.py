import socket
import sys

def get_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return "Nie można znaleźć adresu IP dla podanej nazwy hosta."
    except Exception as e:
        return f"Wystąpił błąd: {e}"

def main():
    hostname = input("Podaj nazwe hosta: ")
    ip_address = get_ip(hostname)
    print(f"Adres IP dla hosta {hostname}: {ip_address}")

if __name__ == "__main__":
    main()
