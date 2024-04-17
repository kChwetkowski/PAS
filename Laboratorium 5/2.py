import socket
import random

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 2010

generated_number = random.randint(1, 100)  # Przedział 1 do 100

def handle_client(client_socket):
    try:
        while True:
            received_data = client_socket.recv(1024)
            client_number = int(received_data.decode())

            if client_number < generated_number:
                client_socket.sendall(b"Twoja liczba jest mniejsza")
            elif client_number == generated_number:
                client_socket.sendall(b"Odgadles")
                return
            else:
                client_socket.sendall(b"Twoja liczba jest wieksza")

    except Exception as e:
        print("Wystąpił błąd podczas obsługi klienta:", e)
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
    server_socket.listen(1)

    print("Serwer nasłuchuje na porcie", SERVER_PORT)
    print("Wygenerowana liczba przez serwer:", generated_number)

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print("Połączono z klientem:", client_address)
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("Przerwano przez użytkownika.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
