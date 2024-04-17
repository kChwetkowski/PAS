import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 2010


def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

        while True:
            try:
                number = int(input("Podaj liczbę: "))
                client_socket.send(str(number).encode())

                received_data = client_socket.recv(1024).decode()
                print("Odpowiedź serwera:", received_data)

                if received_data == "Odgadles":
                    break


            except ValueError:
                print("Podano nieprawidłową liczbę.")

    except Exception as e:
        print("Wystąpił błąd podczas komunikacji z serwerem:", e)
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
