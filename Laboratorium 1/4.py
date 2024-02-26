import socket

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "Nie można znaleźć nazwy hosta dla podanego adresu IP."
    except Exception as e:
        return f"Wystąpił błąd: {e}"

def main():
    ip_address = input("Podaj adres IP: ")
    hostname = get_hostname(ip_address)
    print(f"Nazwa hosta: {hostname}")

if __name__ == "__main__":
    main()
