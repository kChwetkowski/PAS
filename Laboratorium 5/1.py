import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 2912


def send_number(number):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
        client_socket.sendall(str(number).encode())
        received_data = client_socket.recv(1024)

        print("Odgadnięta liczba od serwera:", received_data.decode())

    except Exception as e:
        print("Wystąpił błąd podczas komunikacji z serwerem:", e)

    finally:
        client_socket.close()


def main():
    try:
        number = int(input("Podaj liczbę: "))
        send_number(number)

    except ValueError:
        print("Podano nieprawidłowy input.")


if __name__ == "__main__":
    main()
