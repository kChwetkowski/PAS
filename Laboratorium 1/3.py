import socket

def is_valid_ip(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        return False

def main():
    ip_address = input("Podaj adres IP: ")
    if is_valid_ip(ip_address):
        print("Adres IP jest prawidłowy.")
    else:
        print("Adres IP jest nieprawidłowy.")

if __name__ == "__main__":
    main()
