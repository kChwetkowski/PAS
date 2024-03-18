import socket

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 2010

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:
            num1 = input("Podaj pierwszą liczbę: ")
            op = input("Podaj operator (+, -, *, /): ")
            num2 = input("Podaj drugą liczbę: ")

            message = f"{num1} {op} {num2}"
            client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

            result, server_address = client_socket.recvfrom(1024)
            print(f"Otrzymano wynik od serwera {server_address}: {result.decode()}")

    except socket.error as e:
        print(f"Błąd podczas komunikacji z serwerem: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
