import socket
import sys

SERVICES = {
    20: "FTP (File Transfer Protocol)",
    21: "FTP (File Transfer Protocol)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Hypertext Transfer Protocol)",
    110: "POP3 (Post Office Protocol version 3)",
    143: "IMAP (Internet Message Access Protocol)",
    443: "HTTPS (HTTP Secure)",
    3306: "MySQL",
    3389: "Remote Desktop Protocol (RDP)"
}

def connect_to_server(server_address, server_port):
    try:
        server_ip = socket.gethostbyname(server_address)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  #timeout na 5s
            s.connect((server_ip, server_port))
            service = SERVICES.get(server_port, "Nieznana usługa")
            return True, service
    except Exception as e:
        print(f"Wystąpił błąd podczas łączenia z serwerem: {e}")
        return False, None


def main():
    server_address = input("Podaj adres serwera: ")
    server_port = int(input("Podaj port: "))

    success, service = connect_to_server(server_address, server_port)
    if success:
        print(f"Połączenie z serwerem udane. Usługa na porcie {server_port}: {service}")
    else:
        print("Nie udało się nawiązać połączenia z serwerem.")

if __name__ == "__main__":
    main()
